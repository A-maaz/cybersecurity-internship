import os
from flask import Flask, render_template
from config import config
from models import db, Campaign
from seed_data import seed_database
from routes import main_bp, simulation_bp, dashboard_bp, incident_bp, awareness_bp

def create_app(config_name=None):
    """Application factory for PhishAware educational platform."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
        
    app = Flask(__name__)
    app.config.from_object(config.get(config_name, config['default']))
    
    # Initialize SQLAlchemy
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(simulation_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(incident_bp)
    app.register_blueprint(awareness_bp)
    
    # Custom Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404
        
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500
        
    # Global template context
    @app.context_processor
    def inject_global_data():
        active_campaign = None
        try:
            active_campaign = Campaign.query.filter_by(status='ACTIVE').first()
        except Exception:
            pass
        return {
            'app_name': 'PhishAware',
            'version': '1.0.0',
            'active_campaign': active_campaign,
            'current_year': 2026
        }
        
    # Auto-initialize database and seed demo data if fresh
    with app.app_context():
        db.create_all()
        if Campaign.query.count() == 0:
            try:
                seed_database(app)
            except Exception as e:
                app.logger.warning(f"Initial seed notice: {e}")
                
    return app

if __name__ == '__main__':
    import sys
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    app = create_app('development')
    host = os.environ.get('HOST', '127.0.0.1')
    port = int(os.environ.get('PORT', 5000))
    print("\n" + "="*70)
    print(" [SHIELD] PHISHAWARE - Phishing Awareness Simulation & Incident Response")
    print("    Educational & Authorized Security Training Environment")
    print(f"    Running locally at: http://{host}:{port}")
    print("="*70 + "\n")
    app.run(host=host, port=port, debug=True)
