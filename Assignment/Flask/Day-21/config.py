import os
import secrets

class Config:
    # General settings
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))  # Generate a random 32-character hex string
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://root:root@localhost/employee_portal')