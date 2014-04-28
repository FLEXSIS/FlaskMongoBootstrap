import os

FLASK_APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Flask
from flask import Flask

# Logging
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s',
    datefmt='%Y%m%d-%H:%M%p',
)

app = Flask(__name__)

# Config
if os.getenv('DEV') == 'dev':
    app.config.from_object('flask_application.config.DevelopmentConfig')
    app.logger.info("Config: Development")
elif os.getenv('DEV') == 'test':
    app.config.from_object('flask_application.config.TestConfig')
    app.logger.info("Config: Test")
else:
    app.config.from_object('flask_application.config.ProductionConfig')
    app.logger.info("Config: Production")

# Email on errors
if not app.debug and not app.testing:
    import logging.handlers
    mail_handler = logging.handlers.SMTPHandler(
        'localhost',
        os.getenv('USER'),
        app.config['SYS_ADMINS'],
        '{0} error'.format(app.config['SITE_NAME'],
                           ),
    )
    mail_handler.setFormatter(logging.Formatter('''
Message type:       %(levelname)s
Location:           %(pathname)s:%(lineno)d
Module:             %(module)s
Function:           %(funcName)s
Time:               %(asctime)s

Message:

%(message)s
    '''.strip()))
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
    app.logger.info("Emailing on error is ENABLED")
else:
    app.logger.info("Emailing on error is DISABLED")

# Assets
from flask.ext.assets import Environment
assets = Environment(app)
# Ensure output directory exists
assets_output_dir = os.path.join(FLASK_APP_DIR, 'static', 'gen')
if not os.path.exists(assets_output_dir):
    os.mkdir(assets_output_dir)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 60 * 60 * 24 * 365
# Email
from flask.ext.mail import Mail
mail = Mail(app)

# Helpers
from flask_application.helpers import datetimeformat
app.jinja_env.filters['datetimeformat'] = datetimeformat

from flask.ext.bootstrap import Bootstrap
Bootstrap(app)

# Business Logic
# http://flask.pocoo.org/docs/patterns/packages/
# http://flask.pocoo.org/docs/blueprints/
from flask_application.controllers.frontend import frontend
app.register_blueprint(frontend)

from flask_application.controllers.async import async
app.register_blueprint(async)

from flask.ext.security import Security, MongoEngineUserDatastore
from flask_application.models import db, User, Role
# Setup Flask-Security
user_datastore = MongoEngineUserDatastore(db, User, Role)
app.security = Security(app, user_datastore)

from flask_application.controllers.admin import admin
app.register_blueprint(admin)

# Template filters
import urllib


@app.template_filter('path_slug')
def path_slug(uri, **query):
    return urllib.quote('-'.join(uri.split('/')[1:]))
app.jinja_env.globals['path_slug'] = path_slug

app.jinja_env.globals['hasattr'] = hasattr
