import io
import csv
from flask import Blueprint, render_template, jsonify, Response
from models import Campaign, TestUser, Event, Incident

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard')
def dashboard_view():
    """Renders the SOC-style metrics & telemetry dashboard."""
    # Aggregated metrics
    total_campaigns = Campaign.query.count()
    total_users = TestUser.query.count()
    
    emails_sent = Event.query.filter_by(event_type='EMAIL_SENT').count()
    emails_opened = Event.query.filter_by(event_type='EMAIL_OPENED').count()
    links_clicked = Event.query.filter_by(event_type='LINK_CLICKED').count()
    reports_submitted = Event.query.filter_by(event_type='PHISHING_REPORTED').count()
    training_viewed = Event.query.filter_by(event_type='TRAINING_PAGE_VIEWED').count()
    
    incidents_total = Incident.query.count()
    incidents_resolved = Incident.query.filter_by(status='Resolved').count()
    incidents_active = incidents_total - incidents_resolved
    
    # Calculate rates
    open_rate = round((emails_opened / emails_sent * 100), 1) if emails_sent > 0 else 0.0
    click_rate = round((links_clicked / emails_sent * 100), 1) if emails_sent > 0 else 0.0
    report_rate = round((reports_submitted / emails_sent * 100), 1) if emails_sent > 0 else 0.0
    training_rate = round((training_viewed / links_clicked * 100), 1) if links_clicked > 0 else (100.0 if emails_sent > 0 else 0.0)
    
    # Fetch recent events
    recent_events = Event.query.order_by(Event.timestamp.desc()).limit(20).all()
    
    # Active campaigns
    active_campaigns = Campaign.query.order_by(Campaign.created_at.desc()).all()
    
    # Active incidents
    recent_incidents = Incident.query.order_by(Incident.created_at.desc()).limit(5).all()

    return render_template(
        'dashboard.html',
        total_campaigns=total_campaigns,
        total_users=total_users,
        emails_sent=emails_sent,
        emails_opened=emails_opened,
        links_clicked=links_clicked,
        reports_submitted=reports_submitted,
        training_viewed=training_viewed,
        incidents_total=incidents_total,
        incidents_resolved=incidents_resolved,
        incidents_active=incidents_active,
        open_rate=open_rate,
        click_rate=click_rate,
        report_rate=report_rate,
        training_rate=training_rate,
        recent_events=recent_events,
        active_campaigns=active_campaigns,
        recent_incidents=recent_incidents
    )

@dashboard_bp.route('/api/metrics')
def api_metrics():
    """Provides JSON dataset for dynamic Chart.js rendering."""
    emails_sent = Event.query.filter_by(event_type='EMAIL_SENT').count()
    emails_opened = Event.query.filter_by(event_type='EMAIL_OPENED').count()
    links_clicked = Event.query.filter_by(event_type='LINK_CLICKED').count()
    reports_submitted = Event.query.filter_by(event_type='PHISHING_REPORTED').count()
    training_viewed = Event.query.filter_by(event_type='TRAINING_PAGE_VIEWED').count()
    
    unopened = max(0, emails_sent - emails_opened)
    opened_no_action = max(0, emails_opened - links_clicked - reports_submitted)
    
    # Department Breakdown
    dept_stats = {}
    users = TestUser.query.all()
    for u in users:
        dept = u.department or 'Other'
        if dept not in dept_stats:
            dept_stats[dept] = {'total': 0, 'clicked': 0, 'reported': 0}
        dept_stats[dept]['total'] += 1
        
        if Event.query.filter_by(test_user_id=u.id, event_type='LINK_CLICKED').first():
            dept_stats[dept]['clicked'] += 1
        if Event.query.filter_by(test_user_id=u.id, event_type='PHISHING_REPORTED').first():
            dept_stats[dept]['reported'] += 1

    return jsonify({
        'funnel': {
            'labels': ['Emails Sent', 'Opened', 'Reported (Safe)', 'Clicked (Vulnerable)', 'Completed Training'],
            'data': [emails_sent, emails_opened, reports_submitted, links_clicked, training_viewed]
        },
        'outcomes': {
            'labels': ['Reported Suspicious', 'Clicked Phishing Link', 'Opened (No Action)', 'Unopened'],
            'data': [reports_submitted, links_clicked, opened_no_action, unopened]
        },
        'departments': {
            'labels': list(dept_stats.keys()),
            'clicked': [d['clicked'] for d in dept_stats.values()],
            'reported': [d['reported'] for d in dept_stats.values()]
        }
    })

@dashboard_bp.route('/export/events.csv')
def export_csv():
    """Exports non-sensitive simulation event log as CSV."""
    events = Event.query.order_by(Event.timestamp.asc()).all()
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Header
    writer.writerow(['ID', 'Campaign_ID', 'Test_User', 'Event_Type', 'Timestamp_UTC', 'Source', 'Status', 'Details'])
    for e in events:
        uname = e.test_user.username if e.test_user else 'SYSTEM'
        writer.writerow([
            e.id,
            e.campaign_id,
            uname,
            e.event_type,
            e.timestamp.strftime('%Y-%m-%d %H:%M:%S') if e.timestamp else '',
            e.source,
            e.status,
            e.details
        ])
        
    output.seek(0)
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=phishaware_simulation_events.csv"}
    )
