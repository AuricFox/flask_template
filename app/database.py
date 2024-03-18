import sys, os
from extensions import db
from models.models import Models
from . import utils

LOGGER = utils.LOGGER
PATH = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================================================
def create_tables():
    '''
    Creates the tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are created, else returns false
    '''
    
    try:
        db.create_all()
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when creating tables: {e}")

# ==============================================================================================================
def clear_tables():
    '''
    Deletes the tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are deleted, else returns false
    '''

    try:
        db.drop_all()
        return True
    
    except Exception as e:
        LOGGER.error(f"An error occurred when deleting the tables: {e}")
        return False

# ==============================================================================================================
def main():
    '''
    Handles command line entries to manually set the database tables

    Parameter(s): 
        Two system arguments that include a input flag: 
        python ./init_db.py flag

    flag(s):
        Create tables, "-c", initializes the Flashcard and Figure tables
        Clear tables, "-d", deletes all the rows in both tables

    Output(s): None
    '''

    # python .\phylogeny.py input_file
    if(len(sys.argv) != 2):
        LOGGER.error(f"Only two inputs allowed, {len(sys.argv)} were entered!")

    # Create Tables
    if(sys.argv[1] == "-c"): create_tables()
    # Delete Tables
    elif(sys.argv[1] == "-d"): clear_tables()
    else:
        LOGGER.error(f"Invalid Arguments!\n"
                     f"Create Tables: -c\n"
                     f"Delete Tables: -d\n"
                    )

# ==============================================================================================================
if __name__ == "__main__":
    main()