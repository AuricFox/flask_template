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

# Accessing other pages
@bp.route("/manage")
def users():
    '''
    Processes user page

    Parameter(s): None

    Output(s):
        A rendered HTML user page
    '''
    return render_template('manage.html', nav_id="manage-page")