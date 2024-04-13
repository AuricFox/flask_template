from flask import render_template
from app.main import bp

# ====================================================================
# Main Pages
# ====================================================================
# Accessing Home page
@bp.route("/")
@bp.route("/home")
def index():
    '''
    Processes home page

    Parameter(s): None

    Output(s):
        A rendered HTML home page
    '''
    return render_template('index.html', nav_id="home-page")

# Accessing Manage pages
@bp.route("/manage")
def users():
    '''
    Processes user page

    Parameter(s): None

    Output(s):
        A rendered HTML user page
    '''
    return render_template('./manage/manage.html', nav_id="manage-page")

# ====================================================================
# Login/Sign up
# ====================================================================
@bp.route("/login")
def login():
    '''
    Processes login page

    Parameter(s): None

    Output(s):
        A rendered HTML login page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=False)

@bp.route("/sign_up")
def sign_up():
    '''
    Configures login page to display signup

    Parameter(s): None

    Output(s):
        A rendered HTML login page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=True)