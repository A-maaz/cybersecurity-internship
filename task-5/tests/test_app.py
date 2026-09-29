import unittest
from app import create_app
from models import db, Campaign, TestUser, Event, Incident, IncidentAction

class PhishAwareTestCase(unittest.TestCase):
    """Test suite verifying PhishAware routes, simulation engine, and incident lifecycle."""

    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_homepage_loads(self):
        """Verify homepage renders with 200 OK and SOC title."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'PhishAware', response.data)
        self.assertIn(b'Authorized Training Environment', response.data)

    def test_about_page_loads(self):
        """Verify about page renders with ethics and safety statements."""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Zero Credential Harvesting', response.data)

    def test_demo_seed_endpoint(self):
        """Verify demo seed populates campaign, test users, events, and incident."""
        response = self.client.get('/demo-seed', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(Campaign.query.count(), 1)
        self.assertGreaterEqual(TestUser.query.count(), 10)
        self.assertGreaterEqual(Event.query.count(), 15)
        self.assertGreaterEqual(Incident.query.count(), 1)

    def test_create_simulation_campaign(self):
        """Verify simulation campaign creation with synthetic users."""
        response = self.client.post('/simulation/create', data={
            'name': 'Test Unit Campaign',
            'scenario': 'Account Verification Phishing',
            'sender_profile': 'IT Support <support@test-lab.local>',
            'department': 'Finance',
            'test_user_count': '5'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        campaign = Campaign.query.filter_by(name='Test Unit Campaign').first()
        self.assertIsNotNone(campaign)
        self.assertEqual(len(campaign.test_users), 5)
        
        # Verify EMAIL_SENT events generated
        sent_events = Event.query.filter_by(campaign_id=campaign.id, event_type='EMAIL_SENT').count()
        self.assertEqual(sent_events, 5)

    def test_simulated_email_opening(self):
        """Verify viewing webmail logs EMAIL_OPENED event."""
        # Create campaign and user
        c = Campaign(name='Open Test', scenario='Test Scenario')
        db.session.add(c)
        db.session.flush()
        u = TestUser(username='test-user-01', display_name='User One', campaign_id=c.id)
        db.session.add(u)
        db.session.commit()

        response = self.client.get(f'/simulation/email/{c.id}/{u.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'TechSecure Webmail', response.data)

        # Check event
        open_event = Event.query.filter_by(campaign_id=c.id, test_user_id=u.id, event_type='EMAIL_OPENED').first()
        self.assertIsNotNone(open_event)

    def test_phishing_link_click_and_safe_redirect(self):
        """Verify clicking verification link logs LINK_CLICKED and redirects to safe training."""
        c = Campaign(name='Click Test', scenario='Test Scenario')
        db.session.add(c)
        db.session.flush()
        u = TestUser(username='test-user-02', display_name='User Two', campaign_id=c.id)
        db.session.add(u)
        db.session.commit()

        response = self.client.get(f'/simulation/phishing-link?campaign_id={c.id}&user_id={u.id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Phishing Simulation Detected', response.data)
        self.assertIn(b'No password or sensitive information was collected', response.data)

        # Verify event logged
        click_event = Event.query.filter_by(campaign_id=c.id, test_user_id=u.id, event_type='LINK_CLICKED').first()
        self.assertIsNotNone(click_event)

    def test_employee_report_phishing(self):
        """Verify reporting email logs PHISHING_REPORTED event."""
        c = Campaign(name='Report Test', scenario='Test Scenario')
        db.session.add(c)
        db.session.flush()
        u = TestUser(username='test-user-03', display_name='User Three', campaign_id=c.id)
        db.session.add(u)
        db.session.commit()

        response = self.client.post('/simulation/report-phishing', data={
            'campaign_id': c.id,
            'user_id': u.id
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        report_event = Event.query.filter_by(campaign_id=c.id, test_user_id=u.id, event_type='PHISHING_REPORTED').first()
        self.assertIsNotNone(report_event)

    def test_incident_containment_and_resolution(self):
        """Verify incident response action progression."""
        inc = Incident(
            incident_number='INC-TEST',
            title='Unit Test Incident',
            status='Detected'
        )
        db.session.add(inc)
        db.session.commit()

        # Action 1: Containment
        response = self.client.post(f'/incidents/{inc.id}/action', data={
            'action_type': 'mark_contained',
            'notes': 'Perimeter isolated.'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        inc_reloaded = db.session.get(Incident, inc.id)
        self.assertEqual(inc_reloaded.status, 'Contained')

        # Action 2: Resolution
        response = self.client.post(f'/incidents/{inc.id}/action', data={
            'action_type': 'resolve_incident',
            'notes': 'Remediation completed.'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

        inc_reloaded = db.session.get(Incident, inc.id)
        self.assertEqual(inc_reloaded.status, 'Resolved')
        self.assertIsNotNone(inc_reloaded.resolved_at)

    def test_metrics_api(self):
        """Verify /api/metrics returns correct JSON structure."""
        response = self.client.get('/api/metrics')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('funnel', data)
        self.assertIn('outcomes', data)
        self.assertIn('departments', data)

    def test_csv_export(self):
        """Verify CSV export endpoint returns valid CSV file."""
        response = self.client.get('/export/events.csv')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'text/csv')
        self.assertIn(b'Event_Type', response.data)

    def test_404_error_handler(self):
        """Verify custom 404 page is rendered for invalid paths."""
        response = self.client.get('/nonexistent-route-for-testing')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'404', response.data)

if __name__ == '__main__':
    unittest.main()
