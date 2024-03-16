from flask import render_template
from app.users import bp

# Routes for pages associated with users

@bp.route('/')
def index():
    return render_template('users.html', nav_id="users-page")