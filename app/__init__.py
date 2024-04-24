from flask import Flask, render_template
import os, logging

# Import extensions
from app.extensions import db, login_manager

PATH = os.path.dirname(os.path.abspath(__file__))

# Configure the logging object
logging.basicConfig(
    filename=os.path.join(PATH, '../logs/app.log'),
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s]: %(message)s'
)

LOGGER = logging.getLogger(__name__)

def init_app():
    '''
    Initializes the flask application

    Parameter(s): None

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # NOTE: Configured for development
    app.config.from_object('config.DevConfig')

    # NOTE: Initialize Plugins here
    db.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Custom page not found
    def page_not_found(error):
        return render_template('404.html'), 404
    
    from app.models.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        # NOTE: Include custom modules here
        from . import utils

        # NOTE: Import and register any blueprints here
        from app.main import bp as main_bp
        from app.auth import bp as auth_bp
        from app.manage import bp as manage_bp

        app.register_blueprint(main_bp)
        app.register_blueprint(auth_bp, url_prefix='/auth')
        app.register_blueprint(manage_bp, url_prefix='/manage')
        app.register_error_handler(404, page_not_found)

    return app