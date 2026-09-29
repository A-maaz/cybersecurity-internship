from datetime import datetime, timezone
from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Campaign, TestUser, Event, Incident, IncidentAction

incident_bp = Blueprint('incident', __name__, url_prefix='/incidents')

@incident_bp.route('/')
def incident_list():
    """List all simulated security incidents and their statuses."""
    incidents = Incident.query.order_by(Incident.created_at.desc()).all()
    active_count = Incident.query.filter(Incident.status != 'Resolved').count()
    resolved_count = Incident.query.filter_by(status='Resolved').count()
    
    return render_template(
        'incidents.html',
        incidents=incidents,
        active_count=active_count,
        resolved_count=resolved_count
    )

@incident_bp.route('/create', methods=['POST'])
def create_incident():
    """Manually escalate an incident from a campaign."""
    campaign_id = request.form.get('campaign_id', type=int)
    title = request.form.get('title', 'Simulated Phishing Campaign Escalation')
    severity = request.form.get('severity', 'Medium')
    
    campaign = db.session.get(Campaign, campaign_id) if campaign_id else None
    inc_count = Incident.query.count() + 1
    
    incident = Incident(
        incident_number=f"INC-{inc_count:03d}",
        title=title,
        category="Social Engineering / Phishing",
        severity=severity,
        status="Detected",
        campaign_id=campaign.id if campaign else None,
        detection_indicators=f"Escalated by SOC Analyst for campaign '{campaign.name if campaign else 'Manual'}' based on user reports and link click telemetry.",
        impact_assessment="Simulated scope only. Controlled educational environment. No sensitive data compromised.",
        containment_notes="Pending containment actions.",
        created_at=datetime.now(timezone.utc)
    )
    db.session.add(incident)
    db.session.flush()
    
    # Record initial action
    db.session.add(IncidentAction(
        incident_id=incident.id,
        action="Incident Detected & Ticket Created",
        actor="SOC Analyst (Simulator)",
        timestamp=datetime.now(timezone.utc),
        status="EXECUTED",
        notes="Incident ticket generated in SOC platform."
    ))
    
    # Log event
    if campaign:
        db.session.add(Event(
            campaign_id=campaign.id,
            test_user_id=None,
            event_type='INCIDENT_CREATED',
            timestamp=datetime.now(timezone.utc),
            source='SOC Incident Response',
            status='FLAGGED',
            details=f"Incident {incident.incident_number} escalated for campaign"
        ))
        
    db.session.commit()
    flash(f"Incident {incident.incident_number} successfully registered.", 'success')
    return redirect(url_for('incident.incident_detail', id=incident.id))

@incident_bp.route('/<int:id>')
def incident_detail(id):
    """View incident lifecycle: Detection, Containment, Eradication, Recovery, Timeline."""
    incident = Incident.query.get_or_404(id)
    actions = IncidentAction.query.filter_by(incident_id=id).order_by(IncidentAction.timestamp.desc()).all()
    
    # Fetch related campaign events for timeline reconstruction
    campaign_events = []
    if incident.campaign_id:
        campaign_events = Event.query.filter_by(campaign_id=incident.campaign_id).order_by(Event.timestamp.asc()).all()
        
    return render_template(
        'incident_detail.html',
        incident=incident,
        actions=actions,
        campaign_events=campaign_events
    )

@incident_bp.route('/<int:id>/action', methods=['POST'])
def execute_action(id):
    """Execute simulated containment, eradication, or recovery actions."""
    incident = Incident.query.get_or_404(id)
    action_type = request.form.get('action_type')
    notes = request.form.get('notes', '')
    now = datetime.now(timezone.utc)
    
    actor = "SOC Lead / Analyst (Simulator)"
    action_label = ""
    status_update = None
    
    if action_type == 'disable_campaign':
        action_label = "Disable Campaign"
        notes = notes or "Simulated campaign status flipped to CONTAINED. All inbound simulation dispatches paused."
        if incident.campaign:
            incident.campaign.status = 'CONTAINED'
        incident.containment_notes = (incident.containment_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Campaign disabled."
        if incident.status in ['Detected', 'Analyzing']:
            incident.status = 'Analyzing'
            
    elif action_type == 'block_sender':
        action_label = "Block Simulated Sender"
        notes = notes or "Simulated domain added to transport filter blocklist rules."
        incident.containment_notes = (incident.containment_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Simulated sender blocked."
        
    elif action_type == 'notify_users':
        action_label = "Notify Test Users"
        notes = notes or "Educational warning banner and advisory dispatched to synthetic participants."
        incident.containment_notes = (incident.containment_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Advisory broadcast sent."
        
    elif action_type == 'mark_contained':
        action_label = "Mark Campaign Contained"
        notes = notes or "Containment perimeter confirmed. Phishing simulation threat neutralized."
        incident.status = 'Contained'
        if incident.campaign:
            incident.campaign.status = 'CONTAINED'
        # Log campaign contained event
        if incident.campaign_id:
            db.session.add(Event(
                campaign_id=incident.campaign_id,
                test_user_id=None,
                event_type='CAMPAIGN_CONTAINED',
                timestamp=now,
                source='SOC Incident Response',
                status='CONTAINED',
                details=f"Campaign contained under incident {incident.incident_number}"
            ))
            
    elif action_type == 'disable_link':
        action_label = "Disable Malicious Simulation Link"
        notes = notes or "Simulated URL redirected to Safe Educational Awareness gateway."
        incident.eradication_notes = (incident.eradication_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Verification link deactivated."
        
    elif action_type == 'preserve_evidence':
        action_label = "Preserve Evidence Log"
        notes = notes or "Simulation telemetry hashed and archived for audit compliance."
        incident.eradication_notes = (incident.eradication_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Evidence locked."
        
    elif action_type == 'mark_eradicated':
        action_label = "Mark Eradicated"
        notes = notes or "All malicious artifacts neutralized in training scope."
        incident.status = 'Eradicated'
        
    elif action_type == 'verify_clean':
        action_label = "Verify Simulation Inactive & Clean"
        notes = notes or "Test environment diagnostics confirmed baseline state."
        incident.recovery_notes = (incident.recovery_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Clean state verified."
        
    elif action_type == 'assign_training':
        action_label = "Assign Remedial Awareness Training"
        notes = notes or "Mandatory interactive phishing module assigned to users who interacted with simulation."
        incident.recovery_notes = (incident.recovery_notes or '') + f"\n[{now.strftime('%H:%M:%S')}] Remedial training assigned."
        
    elif action_type == 'resolve_incident':
        action_label = "Incident Resolved"
        notes = notes or "Full response lifecycle completed: Containment, Eradication, and Recovery verified."
        incident.status = 'Resolved'
        incident.resolved_at = now
        if incident.campaign_id:
            db.session.add(Event(
                campaign_id=incident.campaign_id,
                test_user_id=None,
                event_type='INCIDENT_RESOLVED',
                timestamp=now,
                source='SOC Incident Response',
                status='RESOLVED',
                details=f"Incident {incident.incident_number} successfully resolved."
            ))
    else:
        action_label = "Custom Response Action"
        notes = notes or "Custom incident action logged by analyst."
        
    action_record = IncidentAction(
        incident_id=incident.id,
        action=action_label,
        actor=actor,
        timestamp=now,
        status="EXECUTED",
        notes=notes
    )
    db.session.add(action_record)
    db.session.commit()
    
    flash(f"Executed Action: '{action_label}'. Incident state updated.", 'success')
    return redirect(url_for('incident.incident_detail', id=incident.id))

@incident_bp.route('/<int:id>/report')
def incident_report(id):
    """Generates an executive / technical incident report for auditing and portfolio."""
    incident = Incident.query.get_or_404(id)
    actions = IncidentAction.query.filter_by(incident_id=id).order_by(IncidentAction.timestamp.asc()).all()
    campaign_events = []
    if incident.campaign_id:
        campaign_events = Event.query.filter_by(campaign_id=incident.campaign_id).order_by(Event.timestamp.asc()).all()
        
    return render_template(
        'incident_report.html',
        incident=incident,
        actions=actions,
        campaign_events=campaign_events
    )
