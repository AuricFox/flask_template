# Flask Template

This is a template for starting web projects powered by flask. It provides basic navigation for the main pages, sub pages, and a side bar 
for related topics.

## Getting Started

To get started, follow these steps:

1. **Clone the Repository:**
    ```
    git clone https://github.com/AuricFox/flask_template.git
    ```

2. **Navigate to the Project Directory:**
    ```
    cd flask_template
    ```

3. **Setup Environment:**
    ```
    pip install virtualenv  
    virtualenv env

    .\env\Scripts\activate      # Windows
    source env/bin/activate     # Mac OS
    ```

4. **Install Dependencies:**
    ```
    (env) pip install flask python-dotenv Flask-SQLAlchemy
    ```

5. **Run Server:**
    ```
    (env) python wsgi.py
    ```

    The server will start running, and you can access the application by navigating to `http://localhost:5000` in your web browser.

## File Structure

```
.
|-- flask_app
    |-- app
    |   |-- utils.py
    |   |-- __init__.py
    |   |-- main
    |   |   |-- __init__.py
    |   |   |-- routes.py
    |   |-- models
    |   |-- users
    |   |   |-- __init__.py
    |   |   |-- routes.py
    |   |-- static
    |   |   |-- css
    |   |   |   |---base.css
    |   |   |-- images
    |   |   |-- js
    |   |   |   |-- base.js
    |   |-- templates
    |       |-- 404.html
    |       |-- base.html
    |       |-- index.html
    |       |-- users.html
    |-- data
    |   |-- app.db
    |-- logs
    |   |-- app.logs
    |-- .gitignore
    |-- config.py
    |-- wsgi.py
    |-- README.md
    |-- LICENSE
```

## Directories

- **models**: Maintians separation of SQLAlchemy models for large applications. As projects grow, more database tables may be added and more models
will need to be wriiten. Splitting the models into individual files will help with management and maintenance.

- **static**: Contains all the css, js, and image files which are stored in their corresponding directory.

- **templates**: Maintains the organization of the HTML files that provide structure for the web pages.

- **data**: Contains the database and any other possible data management files such as JSON files.

- **logs**: Stores the logging information of the application. Logs info, warnings, and errors as they arise.

- **other**: Any remaining directories (main, etc.) manages the applications blueprints and routes. These enable the end-user to navigate the 
application or website.

## Files

- **config.py**: Configuration file for the Flask application that manages the settings. It configures the `secret key`, `SQLAlchemy database URI`, and more.

- **wsgi.py**: A mediator between the web server and Python web application. Runs the overall application.

## Resources
- [How To Structure a Large Flask Application with Flask Blueprints and Flask-SQLAlchemy](https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy)
- [Demystifying Flask’s “Application Factory”](https://hackersandslackers.com/flask-application-factory/)  
- [User Session Data with Flask-Session & Redis](https://hackersandslackers.com/flask-user-sessions-and-redis/)  
- [Configuring Your Flask App](https://hackersandslackers.com/configure-flask-applications/)  
- [Configuration Handling](https://flask.palletsprojects.com/en/3.0.x/config/#configuration-handling)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.