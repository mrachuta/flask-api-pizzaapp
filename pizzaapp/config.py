"""
This is a defitinion of possible configuration profile
"""

import os

class Local:

    """
    Local environment configuration
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///../dev.sqlite3"
    JWT_SECRET_KEY = "testjwtsecret123"
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Development:

    """
    Development environment configurations
    """

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = f"\
{os.environ.get('FLASK_DB_TYPE')}://\
{os.environ.get('FLASK_DB_USER')}:\
{os.environ.get('FLASK_DB_PASS')}@\
{os.environ.get('FLASK_DB_HOST')}:\
{os.environ.get('FLASK_DB_PORT')}/\
{os.environ.get('FLASK_DB_NAME')}"
    JWT_SECRET_KEY = os.environ.get("FLASK_JWT_SECRET")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class Production:

    """
    Production environment configurations
    """

    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"\
{os.environ.get('FLASK_DB_TYPE')}://\
{os.environ.get('FLASK_DB_USER')}:\
{os.environ.get('FLASK_DB_PASS')}@\
{os.environ.get('FLASK_DB_HOST')}:\
{os.environ.get('FLASK_DB_PORT')}/\
{os.environ.get('FLASK_DB_NAME')}"
    JWT_SECRET_KEY = os.environ.get("FLASK_JWT_SECRET")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    "local": Local,
    "development": Development,
    "production": Production,
}
