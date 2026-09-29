from datetime import datetime, timezone
from flask import Blueprint, render_template, request
from models import db, Campaign, TestUser, Event

awareness_bp = Blueprint('awareness', __name__, url_prefix='/awareness')

@awareness_bp.route('/')
def awareness_view():
    """Renders comprehensive phishing awareness training with indicators and interactive quiz."""
    campaign_id = request.args.get('campaign_id', type=int)
    user_id = request.args.get('user_id', type=int)
    
    user = None
    campaign = None
    if campaign_id and user_id:
        campaign = db.session.get(Campaign, campaign_id)
        user = db.session.get(TestUser, user_id)
        
        # Record training page viewed if not already logged
        if user and campaign:
            existing_training = Event.query.filter_by(
                campaign_id=campaign_id,
                test_user_id=user_id,
                event_type='TRAINING_PAGE_VIEWED'
            ).first()
            
            if not existing_training:
                db.session.add(Event(
                    campaign_id=campaign_id,
                    test_user_id=user_id,
                    event_type='TRAINING_PAGE_VIEWED',
                    timestamp=datetime.now(timezone.utc),
                    source='Security Awareness Portal',
                    status='COMPLETED',
                    details=f"{user.username} completed educational awareness module"
                ))
                db.session.commit()
                
    return render_template('awareness.html', campaign=campaign, user=user)
