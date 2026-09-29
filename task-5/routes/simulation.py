from datetime import datetime, timezone
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Campaign, TestUser, Event, Incident

simulation_bp = Blueprint('simulation', __name__, url_prefix='/simulation')

@simulation_bp.route('/')
def simulation_list():
    """Renders the simulation setup and list of campaigns."""
    campaigns = Campaign.query.order_by(Campaign.created_at.desc()).all()
    recent_events = Event.query.order_by(Event.timestamp.desc()).limit(15).all()
    return render_template('simulation.html', campaigns=campaigns, recent_events=recent_events)

@simulation_bp.route('/create', methods=['POST'])
def create_campaign():
    """Creates a new simulated educational campaign with synthetic test users."""
    name = request.form.get('name', '').strip()
    scenario = request.form.get('scenario', 'Account Verification Phishing')
    sender_profile = request.form.get('sender_profile', 'IT Security <security@techsecure-training.local>')
    department = request.form.get('department', 'Corporate Staff')
    
    try:
        user_count = int(request.form.get('test_user_count', 10))
        user_count = max(1, min(user_count, 50))  # Bound between 1 and 50
    except ValueError:
        user_count = 10
        
    if not name:
        name = f"Simulation Campaign - {scenario}"
        
    now = datetime.now(timezone.utc)
    campaign = Campaign(
        name=name,
        scenario=scenario,
        sender_profile=sender_profile,
        target_department=department,
        status='ACTIVE',
        test_user_count=user_count,
        created_at=now
    )
    db.session.add(campaign)
    db.session.flush()
    
    # Generate synthetic test users
    first_names = ["Alex", "Samantha", "Marcus", "Elena", "Jordan", "David", "Chloe", "Liam", "Priya", "Robert",
                   "Sophia", "Daniel", "Emma", "Oliver", "Maya", "Noah", "Grace", "Ethan", "Zoe", "James"]
    depts = ["Finance", "HR", "Engineering", "Operations", "Marketing", "Sales", "Legal", "Executive"]
    
    test_users = []
    for i in range(1, user_count + 1):
        uname = f"test-user-{i:02d}"
        dname = f"{first_names[(i - 1) % len(first_names)]} (Simulated)"
        user_dept = depts[(i - 1) % len(depts)]
        u = TestUser(username=uname, display_name=dname, department=user_dept, campaign_id=campaign.id)
        db.session.add(u)
        db.session.flush()
        test_users.append(u)
        
    # Log campaign start event
    db.session.add(Event(
        campaign_id=campaign.id,
        test_user_id=None,
        event_type='CAMPAIGN_STARTED',
        timestamp=now,
        source='Simulation Engine',
        status='SUCCESS',
        details=f"Campaign '{name}' launched with {user_count} synthetic recipients"
    ))
    
    # Log EMAIL_SENT events for each synthetic user
    for u in test_users:
        db.session.add(Event(
            campaign_id=campaign.id,
            test_user_id=u.id,
            event_type='EMAIL_SENT',
            timestamp=now,
            source='Simulated Corporate Webmail',
            status='DELIVERED',
            details=f"Simulated message delivered to {u.username} ({u.display_name})"
        ))
        
    db.session.commit()
    flash(f"Campaign '{campaign.name}' successfully launched with {user_count} synthetic test users.", 'success')
    return redirect(url_for('simulation.simulation_detail', id=campaign.id))

@simulation_bp.route('/<int:id>')
def simulation_detail(id):
    """View details of a specific campaign and interact with test users."""
    campaign = Campaign.query.get_or_404(id)
    events = Event.query.filter_by(campaign_id=id).order_by(Event.timestamp.desc()).all()
    test_users = TestUser.query.filter_by(campaign_id=id).all()
    
    # Calculate quick stats for this campaign
    sent_count = Event.query.filter_by(campaign_id=id, event_type='EMAIL_SENT').count()
    opened_count = Event.query.filter_by(campaign_id=id, event_type='EMAIL_OPENED').count()
    clicked_count = Event.query.filter_by(campaign_id=id, event_type='LINK_CLICKED').count()
    reported_count = Event.query.filter_by(campaign_id=id, event_type='PHISHING_REPORTED').count()
    
    return render_template(
        'simulation_detail.html',
        campaign=campaign,
        events=events,
        test_users=test_users,
        sent_count=sent_count,
        opened_count=opened_count,
        clicked_count=clicked_count,
        reported_count=reported_count
    )

@simulation_bp.route('/email/<int:campaign_id>/<int:user_id>')
def email_view(campaign_id, user_id):
    """Simulated corporate email interface seen by a synthetic employee."""
    campaign = Campaign.query.get_or_404(campaign_id)
    user = TestUser.query.get_or_404(user_id)
    
    # Record EMAIL_OPENED event if not already recorded for this user
    existing_open = Event.query.filter_by(
        campaign_id=campaign_id,
        test_user_id=user_id,
        event_type='EMAIL_OPENED'
    ).first()
    
    if not existing_open:
        db.session.add(Event(
            campaign_id=campaign_id,
            test_user_id=user_id,
            event_type='EMAIL_OPENED',
            timestamp=datetime.now(timezone.utc),
            source='Simulated Corporate Webmail',
            status='LOGGED',
            details=f"Email opened by {user.username} ({user.display_name})"
        ))
        db.session.commit()
        
    # Check if user already clicked or reported
    has_clicked = Event.query.filter_by(campaign_id=campaign_id, test_user_id=user_id, event_type='LINK_CLICKED').first() is not None
    has_reported = Event.query.filter_by(campaign_id=campaign_id, test_user_id=user_id, event_type='PHISHING_REPORTED').first() is not None
    
    return render_template(
        'phishing_email.html',
        campaign=campaign,
        user=user,
        has_clicked=has_clicked,
        has_reported=has_reported
    )

@simulation_bp.route('/phishing-link')
def phishing_link():
    """Safe landing link triggered when user clicks the verification button."""
    campaign_id = request.args.get('campaign_id', type=int)
    user_id = request.args.get('user_id', type=int)
    
    campaign = db.session.get(Campaign, campaign_id) if campaign_id else None
    user = db.session.get(TestUser, user_id) if user_id else None
    
    # If campaign is contained by SOC incident response, show blocked notice
    if campaign and campaign.status == 'CONTAINED':
        return render_template('link_blocked.html', campaign=campaign, user=user)
        
    if campaign and user:
        # Record safe LINK_CLICKED event if not already recorded
        existing_click = Event.query.filter_by(
            campaign_id=campaign_id,
            test_user_id=user_id,
            event_type='LINK_CLICKED'
        ).first()
        
        if not existing_click:
            db.session.add(Event(
                campaign_id=campaign_id,
                test_user_id=user_id,
                event_type='LINK_CLICKED',
                timestamp=datetime.now(timezone.utc),
                source='Awareness Gateway',
                status='ALERT',
                details=f"Simulated link clicked by {user.username}; safely routed to awareness landing"
            ))
            
            # Anomaly Detection Hook: check if link clicks exceed threshold to suggest incident creation
            total_clicks = Event.query.filter_by(campaign_id=campaign_id, event_type='LINK_CLICKED').count() + 1
            if total_clicks >= 3:
                # Check if incident exists
                existing_inc = Incident.query.filter_by(campaign_id=campaign_id).first()
                if not existing_inc:
                    inc_count = Incident.query.count() + 1
                    new_incident = Incident(
                        incident_number=f"INC-{inc_count:03d}",
                        title=f"Anomalous Interaction Spikes - Campaign '{campaign.name}'",
                        category="Social Engineering / Phishing",
                        severity="Medium",
                        status="Detected",
                        campaign_id=campaign_id,
                        detection_indicators=f"Autonomous detection rule triggered: {total_clicks} users clicked simulated verification link within simulation timeframe.",
                        impact_assessment="Simulated scope only. No passwords collected or stored.",
                        containment_notes="Pending SOC analyst review.",
                        eradication_notes="",
                        recovery_notes="",
                        lessons_learned="",
                        created_at=datetime.now(timezone.utc)
                    )
                    db.session.add(new_incident)
                    db.session.add(Event(
                        campaign_id=campaign_id,
                        test_user_id=None,
                        event_type='INCIDENT_CREATED',
                        timestamp=datetime.now(timezone.utc),
                        source='SOC Detection Engine',
                        status='FLAGGED',
                        details=f"Auto-generated incident {new_incident.incident_number} due to link click threshold"
                    ))
            db.session.commit()
            
    return render_template('awareness_landing.html', campaign=campaign, user=user)

@simulation_bp.route('/report-phishing', methods=['POST'])
def report_phishing():
    """Simulates an employee reporting a suspicious email via the SOC report button."""
    campaign_id = request.form.get('campaign_id', type=int)
    user_id = request.form.get('user_id', type=int)
    
    campaign = db.session.get(Campaign, campaign_id) if campaign_id else None
    user = db.session.get(TestUser, user_id) if user_id else None
    
    if campaign and user:
        existing_report = Event.query.filter_by(
            campaign_id=campaign_id,
            test_user_id=user_id,
            event_type='PHISHING_REPORTED'
        ).first()
        
        if not existing_report:
            db.session.add(Event(
                campaign_id=campaign_id,
                test_user_id=user_id,
                event_type='PHISHING_REPORTED',
                timestamp=datetime.now(timezone.utc),
                source='Simulated Report Add-in',
                status='SUCCESS',
                details=f"{user.username} flagged and reported simulated phishing message"
            ))
            db.session.commit()
            
        flash(f"Great job! {user.display_name} successfully identified and reported the simulated phishing email. This strengthens corporate defense.", 'success')
        return redirect(url_for('simulation.email_view', campaign_id=campaign_id, user_id=user_id))
        
    flash('Report received.', 'info')
    return redirect(url_for('simulation.simulation_list'))
