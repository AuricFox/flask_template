from flask import render_template, url_for, redirect
from app.manage import bp
from app.extensions import db
from app.models.models import Models
from app.utils import LOGGER

# Routes for pages associated with users

@bp.route('/')
def index():
    data = Models.query.all()
    return render_template('manage.html', nav_id="manage-page", data=data)

# ==============================================================================================================
@bp.route('/view/<key>', methods=['GET', 'POST'])
def view(key):
    '''
    Retrieves the queried data from the database for viewing

    Parameter(s):
        key (int): the primary key of the question being deleted from the database

    Output(s):
        None, redirects to the view page
    '''
    # Get the data upon the first instance of the key
    data = Models.query.filter_by(id=key).first()
    return render_template('manage.html', nav_id="manage-page", data=data)

# ==============================================================================================================
@bp.route('/edit/<key>', methods=['GET', 'POST'])
def edit(key):
    '''
    Retrieves the queried data from the database for editing

    Parameter(s):
        key (int): the primary key of the question being deleted from the database

    Output(s):
        None, redirects to the edit page
    '''
    # Get the data upon the first instance of the key
    data = Models.query.filter_by(id=key).first()
    return render_template('manage.html', nav_id="manage-page", data=data)

# ==============================================================================================================
@bp.route("/delete/<key>")
def delete(key):
    '''
    Deletes the queried data from the database and redirects to manage page

    Parameter(s):
        key (int): the primary key of the question being deleted from the database

    Output(s):
        None, redirects to the manage page
    '''
    try:
        # Query database for question and delete it
        data = Models.query.filter_by(id=key).first()

        if data:
            # Delete the row data
            db.session.delete(data)
            db.session.commit()
            return True  # Return True to indicate successful deletion
        else:
            return False
    
    except Exception as e:
        LOGGER.error(f'An Error occured when deleting the flashcard: {str(e)}')
    
    return redirect(url_for('manage.index'))