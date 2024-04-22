from flask import request, render_template, redirect, url_for
from app.sign_up import bp

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