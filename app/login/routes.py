from flask import request, render_template, redirect, url_for
from app.login import bp

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
    if request.method == 'GET':
        return render_template('login/login.html', nav_id="home-page", sign_up=False)
    
    elif request.method == 'POST':
        name = request.form.get('name', type=str)
        password = request.form.get('password', type=str)   # NOTE: Must be encypted immediately
        
    else:
        return redirect(url_for('page_not_found'))