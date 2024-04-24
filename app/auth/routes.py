from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user
from app.auth import bp

from app.models.models import User
from app.extensions import db
from app.utils import LOGGER

# ====================================================================
# Login Pages
# ====================================================================
@bp.route("/", methods=['GET', 'POST'])
def index():
    '''
    Renders login/sign-up page

    Parameter(s): None

    Output(s):
        A rendered HTML login/sign-up page
    '''
    return render_template('login/login.html', nav_id="home-page", sign_up=False)

# ====================================================================  
@bp.route("/login", methods=['POST'])
def login():
    '''
    Handles login protocol
    
    Parameter(s): None
    
    Output(s):
        A redirect to a HTML page
    '''
    
    name = request.form.get('name', type=str)
    password = request.form.get('password', type=str)
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(name=name, password=password).first()
    # Check if the user exists
    if not user:
        flash('Incorrect username or password!')
        return redirect(url_for('auth.index'))
    
    login_user(user=user, remember=remember)
    return redirect(url_for('main.index'))

# ====================================================================
# Sign Up Pages
# ====================================================================
@bp.route("/sign_up", methods=['POST'])
def sign_up():
    '''
    Configures sign up page

    Parameter(s): None

    Output(s):
        A rendered HTML sign up page
    '''
    # Get form fields
    name = request.form.get('name', type=str)
    email = request.form.get('email', type=str)
    password = request.form.get('password', type=str)

    user = User.query.filter_by(email=email).first()
    # Redirect to the sign up page if the email is already taken
    if user:
        flash('Email address already exists!')
        return redirect(url_for('login.index'))
    
    # Create new user
    new_user = User(name=name, email=email, password=password)

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('main.index'))