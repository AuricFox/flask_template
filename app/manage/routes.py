from flask import render_template, url_for, redirect, request, flash

from app.manage import bp
from app.extensions import db
from app.models.models import Models
from app.app_utils import LOGGER

from app.forms.default_form import DefaultForm

# Routes for pages associated with manage page

@bp.route('/')
def index():
    try:
        data = Models.query.all()
        return render_template('./manage/manage.html', nav_id="manage-page", data=data)
    
    except Exception as e:
        LOGGER.error(f"An error occured when loading management page: {e}")
        return redirect(url_for('main.index'))

# ==============================================================================================================
@bp.route('/view/<int:id>')
def view(id):
    '''
    Retrieves the queried data from the database for viewing

    Parameter(s):
        key (int): the primary key of the question being deleted from the database

    Output(s):
        None, redirects to the view page
    '''
    try:
        # Get the data upon the first instance of the key
        data = Models.query.filter_by(id=id).first()
        return render_template('./manage/view.html', nav_id="manage-page", data=data)
    
    except Exception as e:
        LOGGER.error(f"An error occured when viewing page for ID {id}: {e}")
        return redirect(url_for('manage.index'))

# ==============================================================================================================
@bp.route('/add_info', methods=['GET', 'POST'])
def add_info():
    '''
    Generates an add new data page

    Parameter(s): None

    Output(s):
        Redirects to manage page if the record was successfully added, else returns an add page
    '''
    try:
        # Get form data and varify contents
        form = DefaultForm(request.form)

        if form.validate_on_submit():

            # Adding new data to the database
            new_record = Models(
                name=form.name.data, 
                date=form.date.data, 
                message=form.message.data
            )
            # Committing new data
            db.session.add(new_record)
            db.session.commit()

            return redirect(url_for('manage.index'))

    except Exception as e:
        # Roll back the session in case of an error
        db.session.rollback()
        LOGGER.error(f"An Error occurred when adding data to the database: {e}")
        flash("Failed to add record!", "error")

    return render_template('./manage/add.html', nav_id="add-page", form=form)

# ==============================================================================================================
@bp.route('/update_info/<int:id>', methods=['GET','POST'])
def update_info(id):
    '''
    Processes the new data and updates the database
    
    Parameter(s): 
        id (int): the primary key of the record being updated

    Output(s):
        Redirects to the manage page if record was successfully added, else returns an edit page
    '''
    try:
        record = Models.query.get(id)
    
        # Check if the record exists
        if record is None:
            flash("Record not found.")
            return redirect(request.referrer or url_for('manage.index'))
    
        # Get form data and varify contents
        form = DefaultForm(form=request.form)
        if form.validate_on_submit():
                
                if form.name.data:
                    record.name = form.name.data
                if form.date.data:
                    record.date = form.date.data
                if form.message.data:
                    record.message = form.message.data
    
                # Commit new data to the database
                db.session.commit()
    
                return redirect(url_for('manage.index'))

    except Exception as e:
        # Roll back the session in case of an error
        db.session.rollback()
        LOGGER.error(f"An Error occurred when updating record: {e}")
        flash("Failed to update record!", "error")

    return render_template('./manage/edit.html', nav_id="manage-page", data=record, form=form)

# ==============================================================================================================
@bp.route("/delete/<int:id>")
def delete(id):
    '''
    Deletes the queried data from the database and redirects to manage page

    Parameter(s):
        key (int): the primary key of the question being deleted from the database

    Output(s):
        None, redirects to the manage page
    '''
    try:
        # Query database for question and delete it
        data = Models.query.filter_by(id=id).first()

        if data:
            # Delete the row data
            db.session.delete(data)
            db.session.commit()
            LOGGER.info(f'Record deleted:\n{data}')
            flash("Successfully deleted record!", "error")
        else:
            LOGGER.error(f'An error occurred when deleting record: {e}')
            flash("Failed to delete record", "error")
    
    except Exception as e:
        LOGGER.error(f'An Error occured when deleting the record: {str(e)}')
    
    return redirect(url_for('manage.index'))