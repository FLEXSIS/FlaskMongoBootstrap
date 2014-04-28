class Config(object):
    SECRET_KEY = '{SECRET_KEY}'
    SITE_NAME = 'Flask Site'
    SITE_ROOT_URL = 'http://example.com'
    MEMCACHED_SERVERS = ['localhost:11211']
    SYS_ADMINS = ['foo@example.com']

    # Mongodb support
    MONGODB_DB = 'testing'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'username'
    MONGODB_PASSWORD = 'password'

    # Configured for GMAIL
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'username@gmail.com'
    MAIL_PASSWORD = '*********'
    DEFAULT_MAIL_SENDER = 'A.N. Sender < sender@example.com >'
    SECURITY_EMAIL_SENDER = 'A.N. Sender < sender@example.com >'

    # Flask-Security setup
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_PASSWORD_HASH = 'A-HA$H'
    SECURITY_PASSWORD_SALT = 'SuMs@lT'
    SECURITY_REGISTERABLE = True
    SECURITY_RECOVERABLE = True
    SECURITY_CHANGEABLE = True
    SECURITY_URL_PREFIX = '/auth'
    SECUIRTY_POST_LOGIN = '/'

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECURITY_CONFIRMABLE = True
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = False

    # Mongodb production
    MONGODB_DB = 'production#'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27017
    MONGODB_USERNAME = 'username'
    MONGODB_PASSWORD = 'password'

class TestConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    DEBUG = False
    TESTING = True

class DevelopmentConfig(Config):
    SITE_ROOT_URL = 'http://localhost:5000'
    '''Use "if app.debug" anywhere in your code, that code will run in development code.'''
    DEBUG = True
    TESTING = True

