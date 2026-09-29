from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Campaign(db.Model):
    """Represents a simulated educational phishing campaign."""
    __tablename__ = 'campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    scenario = db.Column(db.String(120), nullable=False, default='Account Verification Phishing')
    sender_profile = db.Column(db.String(150), default='IT Security <security@techsecure-training.local>')
    target_department = db.Column(db.String(80), default='All Departments')
    status = db.Column(db.String(30), default='ACTIVE')  # ACTIVE, CONTAINED, COMPLETED, DRAFT
    test_user_count = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    
    # Relationships
    test_users = db.relationship('TestUser', backref='campaign', cascade='all, delete-orphan', lazy=True)
    events = db.relationship('Event', backref='campaign', cascade='all, delete-orphan', lazy=True)
    incidents = db.relationship('Incident', backref='campaign', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'scenario': self.scenario,
            'sender_profile': self.sender_profile,
            'target_department': self.target_department,
            'status': self.status,
            'test_user_count': self.test_user_count,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None
        }

class TestUser(db.Model):
    """Represents a synthetic, fictional employee in the simulation."""
    __tablename__ = 'test_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    display_name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(80), default='Operations')
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    
    # Relationships
    events = db.relationship('Event', backref='test_user', cascade='all, delete-orphan', lazy=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'display_name': self.display_name,
            'department': self.department,
            'campaign_id': self.campaign_id
        }

class Event(db.Model):
    """Records safe, non-sensitive educational simulation telemetry."""
    __tablename__ = 'events'
    
    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=False)
    test_user_id = db.Column(db.Integer, db.ForeignKey('test_users.id'), nullable=True)
    event_type = db.Column(db.String(50), nullable=False)
    # Types: CAMPAIGN_STARTED, EMAIL_SENT, EMAIL_OPENED, LINK_CLICKED, 
    #        TRAINING_PAGE_VIEWED, PHISHING_REPORTED, CAMPAIGN_CONTAINED,
    #        CAMPAIGN_COMPLETED, INCIDENT_CREATED, INCIDENT_CONTAINED, INCIDENT_RESOLVED
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    source = db.Column(db.String(100), default='Simulated Corporate Webmail')
    status = db.Column(db.String(50), default='LOGGED')
    details = db.Column(db.String(255), default='')
    
    def to_dict(self):
        return {
            'id': self.id,
            'campaign_id': self.campaign_id,
            'test_user': self.test_user.username if self.test_user else 'SYSTEM',
            'test_user_id': self.test_user_id,
            'event_type': self.event_type,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S') if self.timestamp else None,
            'time_only': self.timestamp.strftime('%H:%M:%S') if self.timestamp else '',
            'source': self.source,
            'status': self.status,
            'details': self.details
        }

class Incident(db.Model):
    """Represents a simulated cybersecurity incident triggered by simulation anomalies."""
    __tablename__ = 'incidents'
    
    id = db.Column(db.Integer, primary_key=True)
    incident_number = db.Column(db.String(30), unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    category = db.Column(db.String(100), default='Social Engineering / Phishing')
    severity = db.Column(db.String(30), default='Medium')  # Low, Medium, High, Critical
    status = db.Column(db.String(30), default='Detected')  # Detected, Analyzing, Contained, Eradicated, Recovered, Resolved
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaigns.id'), nullable=True)
    
    # Audit & Lifecycle fields
    detection_indicators = db.Column(db.Text, default='')
    impact_assessment = db.Column(db.Text, default='')
    containment_notes = db.Column(db.Text, default='')
    eradication_notes = db.Column(db.Text, default='')
    recovery_notes = db.Column(db.Text, default='')
    lessons_learned = db.Column(db.Text, default='')
    
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    resolved_at = db.Column(db.DateTime, nullable=True)
    
    # Relationships
    actions = db.relationship('IncidentAction', backref='incident', cascade='all, delete-orphan', lazy=True, order_by='IncidentAction.timestamp.desc()')
    
    def to_dict(self):
        return {
            'id': self.id,
            'incident_number': self.incident_number,
            'title': self.title,
            'category': self.category,
            'severity': self.severity,
            'status': self.status,
            'campaign_id': self.campaign_id,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S') if self.created_at else None,
            'resolved_at': self.resolved_at.strftime('%Y-%m-%d %H:%M:%S') if self.resolved_at else None,
            'action_count': len(self.actions)
        }

class IncidentAction(db.Model):
    """Records containment, eradication, and recovery actions taken during incident response."""
    __tablename__ = 'incident_actions'
    
    id = db.Column(db.Integer, primary_key=True)
    incident_id = db.Column(db.Integer, db.ForeignKey('incidents.id'), nullable=False)
    action = db.Column(db.String(150), nullable=False)
    actor = db.Column(db.String(100), default='SOC Analyst (Simulator)')
    timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    status = db.Column(db.String(50), default='EXECUTED')
    notes = db.Column(db.Text, default='')
    
    def to_dict(self):
        return {
            'id': self.id,
            'incident_id': self.incident_id,
            'action': self.action,
            'actor': self.actor,
            'timestamp': self.timestamp.strftime('%Y-%m-%d %H:%M:%S') if self.timestamp else None,
            'time_only': self.timestamp.strftime('%H:%M:%S') if self.timestamp else '',
            'status': self.status,
            'notes': self.notes
        }
