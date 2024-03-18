from flask import render_template
from app.manage import bp
from app.extensions import db
from app.models.models import Models

# Routes for pages associated with users

@bp.route('/')
def index():
    data = Models.query.all()
    return render_template('manage.html', nav_id="manage-page", data=data)