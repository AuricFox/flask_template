# Creating a blueprint for login and sign-up pages
from flask import Blueprint
bp = Blueprint('sign_up', __name__)
from app.sign_up import routes