import os
from dotenv import load_dotenv
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False  # debug mode
    TESTING = False  # testing mode
    CSRF_ENABLED = True  # CSRF prevention
    SECRET_KEY = os.getenv('secret_key')  # server secret


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
