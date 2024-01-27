from flask import Blueprint
from .controllers import AuthController

auth = Blueprint('auth', __name__)

base_url = '/auth'

@auth.route(f'{base_url}/login', methods=["POST"])
def login():
    return AuthController.login()
    