from flask import Flask
# Impport need libraries
# from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
# db = SQLAlchemy()

def init_app():
    '''
    Initializes the flask application

    Parameter(s): None

    Output(s):
        app (Object): flask application object
    '''
    app = Flask(__name__, instance_relative_config=False)
    # Configured for development
    app.config.from_object('config.DevConfig')

    # NOTE: Initialize Plugins here
    #db.init_app(app)

    with app.app_context():
        # NOTE: Include routes and custom modules here
        from . import routes
        from . import utils

        # NOTE: Register any blueprints here
        #app.register_blueprint(auth.auth_bp)
        #app.register_blueprint(admin.admin_bp)

    return app