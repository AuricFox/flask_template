from flask import render_template
from app.login import bp

# ====================================================================
# Login Pages
# ====================================================================
@bp.route("/")
def index():
    '''
    Processes login page

    Parameter(s): None

    Output(s):
        A rendered HTML login page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=False)