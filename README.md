# flask_template

This is a template for starting web projects powered by flask.

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
    (env) pip install flask python-dotenv
    ```

5. **Run Server:**
    ```
    (env) python wsgi.py
    ```

    The server will start running, and you can access the application by navigating to `http://localhost:5000` in your web browser.

## Resources

[Demystifying Flask’s “Application Factory”](https://hackersandslackers.com/flask-application-factory/)  
[User Session Data with Flask-Session & Redis](https://hackersandslackers.com/flask-user-sessions-and-redis/)  
[Configuring Your Flask App](https://hackersandslackers.com/configure-flask-applications/)  
[Configuration Handling](https://flask.palletsprojects.com/en/3.0.x/config/#configuration-handling)

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.
