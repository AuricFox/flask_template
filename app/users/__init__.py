# Creating a blueprint for user pages
from flask import Blueprint
bp = Blueprint('users', __name__)
from app.users import routes