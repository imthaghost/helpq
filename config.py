import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))
# load enviornment variables
load_dotenv()


class Config(object):
    DEBUG = False  # debug mode
    TESTING = False  # testing mode
    CSRF_ENABLED = True  # CSRF prevention
    SECRET_KEY = os.getenv('secret_key')  # server secret
    MONGODB_URI = os.getenv('DATABASE_URL')


class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    SERVER_NAME = 'makehelpqueue.herokuapp.com'
    FLASK_ENV = 'production'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVER_NAME = '127.0.0.1:8000'
    FLASK_ENV = 'development'


class TestingConfig(Config):
    TESTING = True
