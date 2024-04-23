from flask import request, render_template, redirect, url_for
from flask_login import login_user
from app.auth import bp

from app.models.models import User

# ====================================================================
# Login Pages
# ====================================================================
@bp.route("/", methods=['GET', 'POST'])
def index():
    '''
    Processes login page

    Parameter(s): None

    Output(s):
        A rendered HTML login page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=False)

# ====================================================================  
@bp.route("/login", methods=['GET', 'POST'])
def login():
    '''
    Handles login protocol
    
    Parameter(s): None
    
    Output(s):
        A redirect to a HTML page
    '''
    
    name = request.form.get('name', type=str)
    password = request.form.get('password', type=str)   # NOTE: Must be encypted immediately

# ====================================================================
# Sign Up Pages
# ====================================================================
@bp.route("/")
def index():
    '''
    Configures sign up page

    Parameter(s): None

    Output(s):
        A rendered HTML sign up page
    '''
    if request.method == 'GET':
        return render_template('login/login.html', nav_id="home-page", sign_up=False)
    
    elif request.method == 'POST':
        name = request.form.get('name', type=str)
        email = request.form.get('email', type=str)
        password = request.form.get('password', type=str)   # NOTE: Must be encypted immediately
        
    else:
        return redirect(url_for('404'))