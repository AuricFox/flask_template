from flask import render_template
from app.sign_up import bp

# ====================================================================
# Sign Up Pages
# ====================================================================
@bp.route("/")
def index():
    '''
    Configures login page to display signup

    Parameter(s): None

    Output(s):
        A rendered HTML login page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=True)