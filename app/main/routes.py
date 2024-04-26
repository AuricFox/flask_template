from flask import render_template
from flask_login import login_required, current_user
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
    return render_template('index.html', nav_id="home-page", username=current_user.name)

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