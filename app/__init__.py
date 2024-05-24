from flask import Flask, render_template
import os, logging

# Import extensions
from app.extensions import db
from flask_wtf.csrf import CSRFProtect

PATH = os.path.dirname(os.path.abspath(__file__))

# Configure the logging object
logging.basicConfig(
    filename=os.path.join(PATH, '../logs/app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

LOGGER = logging.getLogger(__name__)

def init_app(configure='config.DevConfig'):
    '''
    Initializes the flask application

    Parameter(s):
        configure (default='config.DevConfig'): app environment configuration

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # NOTE: Configured for development
    app.config.from_object(configure)

    # NOTE: Initialize Plugins here
    db.init_app(app)
    CSRFProtect(app)

    # Custom page not found
    def page_not_found(error):
        return render_template('404.html'), 404

    with app.app_context():
        # NOTE: Include custom modules here
        from . import app_utils

        # NOTE: Import and register any blueprints here
        from app.main import bp as main_bp
        from app.manage import bp as manage_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(manage_bp, url_prefix='/manage')
        app.register_error_handler(404, page_not_found)

    return app