from flask import Blueprint
from .controllers import login

auth = Blueprint('auth', __name__)

base_url = '/auth'

@auth.route(f'{base_url}/login', methods=["POST"])
def post_login():
    return login()
    