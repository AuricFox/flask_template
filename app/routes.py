from flask import request, render_template
from . import utils

# Run Flask server using current application
from flask import current_app as app

# Global variable used for logging info, warnings, or errors
LOGGER = utils.LOGGER

# ====================================================================
# Main Page(s)
# ====================================================================
@app.route("/")
@app.route("/index")
@app.route("/home")
def home():
    '''
    Processes home page

    Parameter(s): None

    Output(s):
        A rendered HTML home page
    '''

    return render_template('home.html')

# ====================================================================
# Custom page not found
'''@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404'''