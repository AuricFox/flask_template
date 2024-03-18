import sqlite3, sys, os
from tabulate import tabulate
from . import utils

LOGGER = utils.LOGGER
PATH = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================================================
def create_tables():
    '''
    Creates the Figure and Flashcards tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are created, else returns false
    '''
    
    try:
        with sqlite3.connect('flashcards.db') as conn:      

            c = conn.cursor()
            # Force forgein key support
            c.execute("PRAGMA foreign_keys = ON;")

            # Code elements for supporting the flashcard
            LOGGER.info("Creating Figure Table...")
            c.execute("""CREATE TABLE Figure(
                    fid INTEGER PRIMARY KEY AUTOINCREMENT,
                    code_block TEXT,
                    code_type TEXT,
                    image_file TEXT
            )""")
        
            # Main flashcard elements
            LOGGER.info("Creating Flashcard Table...")
            c.execute("""CREATE TABLE Flashcards(
                    cid INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    question TEXT,
                    answer TEXT,
                    qid INTEGER REFERENCES Figure(fid), 
                    aid INTEGER REFERENCES Figure(fid)
            )""")

            conn.commit()
        
        return True
        
    except Exception as e:
        LOGGER.error(f"An error occured when creating tables: {e}")

# ==============================================================================================================
def clear_tables():
    '''
    Wipes the data from the Figure and Flashcards tables used by the flask server.

    Parameter(s): None

    Output(s): 
        Bool: returns true if the tables are wiped, else returns false
    '''

    try:
        with sqlite3.connect('flashcards.db') as conn:
            c = conn.cursor()

            # Clear Flashcard table
            LOGGER.info("DELETE FROM Flashcards")
            c.execute("DELETE FROM Flashcards")

            # Clear Figure table (images and code)
            LOGGER.info("DELETE FROM Figure")
            c.execute("DELETE FROM Figure")

            conn.commit()

            # Get path to saved flashcard images
            folder = os.path.join(PATH, './static/images/web_images/')

            # Remove saved image files
            for file in os.listdir(folder):
                os.remove(os.path.join(PATH, file))

        return True
    
    except sqlite3.Error as e:
        LOGGER.error(f"An error occurred when deleting all records from the tables: {e}")
        return False

# ==============================================================================================================
def print_tables():
    '''
    Prints the contents of the Flashcards and Figure Tables.

    Parameter(s): None

    Output(s): None
    '''

    with sqlite3.connect('flashcards.db') as conn:
            c = conn.cursor()

            # Print Figure table data
            print("Figure Table Data:")
            c.execute("SELECT * FROM Figure")
            q_figures = c.fetchall()
            print(tabulate(q_figures, headers=["fid", "code_block", "code_type", "image_file"], tablefmt="grid"))

            # Print Flashcards table data
            print("Flashcards Table Data:")
            c.execute("SELECT * FROM Flashcards")
            q_cards = c.fetchall()
            print(tabulate(q_cards, headers=["cid", "category", "question", "answer", "qid", "aid"], tablefmt="grid"))

            conn.commit()

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
        Print tables, "-p", prints all the rows in both tables

    Output(s): None
    '''

    # python .\phylogeny.py input_file
    if(len(sys.argv) != 2):
        LOGGER.error(f"Only two inputs allowed, {len(sys.argv)} were entered!")

    # Create Tables
    if(sys.argv[1] == "-c"): create_tables()
    # Delete Tables
    elif(sys.argv[1] == "-d"): clear_tables()
    # Print Tables
    elif(sys.argv[1] == "-p"): print_tables()
    else:
        LOGGER.error(f"Invalid Arguments!\n"
                     f"Create Tables: -c\n"
                     f"Delete Tables: -d\n"
                     f"Print Tables: -p\n"
                    )

# ==============================================================================================================
if __name__ == "__main__":
    main()