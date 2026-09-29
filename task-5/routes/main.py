from flask import Blueprint, render_template, redirect, url_for, flash, current_app
from models import db, Campaign, TestUser, Event, Incident
from seed_data import seed_database

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Renders the SOC-inspired homepage."""
    total_campaigns = Campaign.query.count()
    active_campaign = Campaign.query.filter_by(status='ACTIVE').first() or Campaign.query.first()
    total_users = TestUser.query.count()
    total_events = Event.query.count()
    total_incidents = Incident.query.count()
    resolved_incidents = Incident.query.filter_by(status='Resolved').count()
    
    return render_template(
        'index.html',
        total_campaigns=total_campaigns,
        active_campaign=active_campaign,
        total_users=total_users,
        total_events=total_events,
        total_incidents=total_incidents,
        resolved_incidents=resolved_incidents
    )

@main_bp.route('/about')
def about():
    """Renders the about page detailing educational scope and safety guarantees."""
    return render_template('about.html')

@main_bp.route('/demo-seed', methods=['GET', 'POST'])
def demo_seed():
    """Seeds synthetic test data for instant demonstration and video presentation."""
    try:
        seed_database(current_app)
        flash('Demo Mode Activated: Synthetic simulation campaign, 10 test users, telemetry, and incident successfully seeded.', 'success')
    except Exception as e:
        flash(f'Error seeding demo data: {str(e)}', 'danger')
    return redirect(url_for('dashboard.dashboard_view'))

@main_bp.route('/reset-data', methods=['POST'])
def reset_data():
    """Resets database to clean slate for a fresh simulation run."""
    try:
        db.drop_all()
        db.create_all()
        flash('All simulation data has been reset to a clean state.', 'info')
    except Exception as e:
        flash(f'Error resetting database: {str(e)}', 'danger')
    return redirect(url_for('main.index'))
