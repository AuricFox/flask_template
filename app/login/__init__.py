# Creating a blueprint for login pages
from flask import Blueprint
bp = Blueprint('login', __name__)
from app.login import routes