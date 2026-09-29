import os
from pathlib import Path

# Base directory of the application
BASE_DIR = Path(__file__).resolve().parent

class Config:
    """Base application configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'phishaware-safe-educational-secret-key-2026')
    
    # Ensure database directory exists
    DB_DIR = BASE_DIR / 'database'
    DB_DIR.mkdir(parents=True, exist_ok=True)
    
    DB_PATH = DB_DIR / 'app.db'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', f"sqlite:///{DB_PATH.as_posix()}")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session cookie hardening
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Simulation settings (strictly safe and educational)
    SIMULATION_MODE = 'CONTROLLED_EDUCATIONAL'
    MAX_TEST_USERS_PER_CAMPAIGN = 50
    ALLOW_CREDENTIAL_STORAGE = False  # Hard safety lock: never allow credential storage

class DevelopmentConfig(Config):
    """Development configuration with debugging enabled."""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration with safety locks."""
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE = True

class TestingConfig(Config):
    """Testing configuration with in-memory database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
