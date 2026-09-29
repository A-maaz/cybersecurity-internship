"""
Database initialization and synthetic demo data seeder.
Ensures zero sensitive data collection; only synthetic test fixtures.
"""

from datetime import datetime, timedelta, timezone
from models import db, Campaign, TestUser, Event, Incident, IncidentAction

def seed_database(app):
    """Populates the database with realistic synthetic simulation data for demo & presentation."""
    with app.app_context():
        # Clear existing records
        db.drop_all()
        db.create_all()
        
        base_time = datetime.now(timezone.utc) - timedelta(hours=2)
        
        # 1. Create Default Demo Campaign
        campaign = Campaign(
            name="Security Verification Awareness Test",
            scenario="Account Verification Phishing",
            sender_profile="IT Security <security@techsecure-training.local>",
            target_department="Corporate All-Staff",
            status="ACTIVE",
            test_user_count=10,
            created_at=base_time
        )
        db.session.add(campaign)
        db.session.flush()
        
        # 2. Create 10 Synthetic Test Users
        departments = [
            ("test-user-01", "Alex Morgan", "Finance"),
            ("test-user-02", "Samantha Reed", "HR"),
            ("test-user-03", "Marcus Chen", "Engineering"),
            ("test-user-04", "Elena Rostova", "Operations"),
            ("test-user-05", "Jordan Taylor", "Marketing"),
            ("test-user-06", "David Kim", "Sales"),
            ("test-user-07", "Chloe Bennett", "Finance"),
            ("test-user-08", "Liam Wright", "Engineering"),
            ("test-user-09", "Priya Patel", "Legal"),
            ("test-user-10", "Robert Sterling", "Executive")
        ]
        
        test_users = {}
        for username, display_name, dept in departments:
            user = TestUser(
                username=username,
                display_name=display_name,
                department=dept,
                campaign_id=campaign.id
            )
            db.session.add(user)
            db.session.flush()
            test_users[username] = user
        
        # 3. Create Events (Matching: 10 Sent, 8 Opened, 4 Clicked, 6 Reported, 4 Training Completed)
        # Event 1: Campaign Started
        db.session.add(Event(
            campaign_id=campaign.id,
            test_user_id=None,
            event_type='CAMPAIGN_STARTED',
            timestamp=base_time,
            source='Simulation Engine',
            status='SUCCESS',
            details='Campaign initialized with 10 synthetic test recipients'
        ))
        
        # 10 Emails Sent
        for i, (uname, _, _) in enumerate(departments):
            db.session.add(Event(
                campaign_id=campaign.id,
                test_user_id=test_users[uname].id,
                event_type='EMAIL_SENT',
                timestamp=base_time + timedelta(minutes=1, seconds=i*4),
                source='Simulated Corporate Webmail',
                status='DELIVERED',
                details=f'Simulated message dispatched to {uname}'
            ))
            
        # 8 Emails Opened (users 1, 2, 3, 4, 5, 6, 7, 8)
        opened_users = ['test-user-01', 'test-user-02', 'test-user-03', 'test-user-04', 
                        'test-user-05', 'test-user-06', 'test-user-07', 'test-user-08']
        for i, uname in enumerate(opened_users):
            db.session.add(Event(
                campaign_id=campaign.id,
                test_user_id=test_users[uname].id,
                event_type='EMAIL_OPENED',
                timestamp=base_time + timedelta(minutes=2 + (i // 3), seconds=(i * 18) % 60),
                source='Simulated Corporate Webmail',
                status='LOGGED',
                details=f'{uname} opened simulated message'
            ))
            
        # 4 Links Clicked (users 1, 4, 7, 8)
        clicked_users = ['test-user-01', 'test-user-04', 'test-user-07', 'test-user-08']
        for i, uname in enumerate(clicked_users):
            db.session.add(Event(
                campaign_id=campaign.id,
                test_user_id=test_users[uname].id,
                event_type='LINK_CLICKED',
                timestamp=base_time + timedelta(minutes=4, seconds=10 + i * 25),
                source='Awareness Gateway',
                status='ALERT',
                details=f'{uname} clicked simulated verification link; safely redirected to training'
            ))
            
        # 6 Reported Phishing (users 2, 3, 5, 6, 9, 10)
        reported_users = ['test-user-02', 'test-user-03', 'test-user-05', 'test-user-06', 'test-user-09', 'test-user-10']
        for i, uname in enumerate(reported_users):
            db.session.add(Event(
                campaign_id=campaign.id,
                test_user_id=test_users[uname].id,
                event_type='PHISHING_REPORTED',
                timestamp=base_time + timedelta(minutes=5, seconds=15 + i * 30),
                source='Simulated Report Add-in',
                status='SUCCESS',
                details=f'{uname} flagged email using PhishAware Report button'
            ))
            
        # Incident Created Triggered at 09:06
        incident_time = base_time + timedelta(minutes=6, seconds=30)
        db.session.add(Event(
            campaign_id=campaign.id,
            test_user_id=None,
            event_type='INCIDENT_CREATED',
            timestamp=incident_time,
            source='SOC Detection Engine',
            status='FLAGGED',
            details='Incident INC-001 automatically opened due to simulated link interaction threshold'
        ))
        
        # 4 Training Page Viewed (users 1, 4, 7, 8)
        for i, uname in enumerate(clicked_users):
            db.session.add(Event(
                campaign_id=campaign.id,
                test_user_id=test_users[uname].id,
                event_type='TRAINING_PAGE_VIEWED',
                timestamp=base_time + timedelta(minutes=10, seconds=i * 20),
                source='Security Awareness Portal',
                status='COMPLETED',
                details=f'{uname} reviewed educational indicators and completed training review'
            ))
            
        # 4. Create Simulated Incident INC-001
        incident = Incident(
            incident_number="INC-001",
            title="Simulated Phishing Campaign - Credential Verification Vector",
            category="Social Engineering / Phishing",
            severity="Medium",
            status="Contained",
            campaign_id=campaign.id,
            detection_indicators="Multiple simulated link clicks (4 test users) combined with 6 proactive user reports received within 5 minutes. Detection rule: PHISH-SIM-RULE-104 triggered.",
            impact_assessment="Simulated scope: 10 test mailboxes targeted in educational exercise. 4 test users interacted with harmless landing page. Zero sensitive data compromised. Zero credentials collected.",
            containment_notes="Simulated campaign deactivated. Local simulation link neutralized. Warning banner injected to simulated mailboxes.",
            eradication_notes="Verification that simulation URL redirects to educational awareness module. Test campaign artifacts cataloged.",
            recovery_notes="Safe test environment verified. Automated remedial training module assigned to test users who clicked.",
            lessons_learned="Highlight need for domain spoofing awareness. User reporting speed was commendable (6 reports under 6 minutes).",
            created_at=incident_time,
            resolved_at=None
        )
        db.session.add(incident)
        db.session.flush()
        
        # Incident Actions Timeline
        actions = [
            ("Incident Detected", "Automated SIEM / SOC Detection Engine", incident_time, "EXECUTED", "Threshold anomaly triggered ticket creation"),
            ("Analyze Threat Indicators", "Tier 1 SOC Analyst", incident_time + timedelta(minutes=1), "EXECUTED", "Confirmed simulated sender profile and fake verification link"),
            ("Disable Campaign", "SOC Lead", incident_time + timedelta(minutes=2), "EXECUTED", "Simulated campaign status flipped to CONTAINED"),
            ("Block Simulated Sender", "Mail Security Admin", incident_time + timedelta(minutes=2, seconds=30), "EXECUTED", "Simulated domain added to transport filter blocklist"),
            ("Notify Test Users", "Internal Security Comms", incident_time + timedelta(minutes=3), "EXECUTED", "Sent safe educational advisory notice to all 10 participants"),
            ("Mark Campaign Contained", "Incident Commander", incident_time + timedelta(minutes=3, seconds=45), "EXECUTED", "Simulated threat neutralized in training environment")
        ]
        
        for act_name, actor, act_time, act_status, act_notes in actions:
            db.session.add(IncidentAction(
                incident_id=incident.id,
                action=act_name,
                actor=actor,
                timestamp=act_time,
                status=act_status,
                notes=act_notes
            ))
            
        # Campaign contained event
        db.session.add(Event(
            campaign_id=campaign.id,
            test_user_id=None,
            event_type='CAMPAIGN_CONTAINED',
            timestamp=incident_time + timedelta(minutes=3, seconds=45),
            source='SOC Incident Response',
            status='CONTAINED',
            details='Simulation link disabled and test sender blocked'
        ))
        
        db.session.commit()
        print("Database successfully seeded with synthetic demo records.")

if __name__ == '__main__':
    from app import create_app
    app = create_app('development')
    seed_database(app)
