from flask import Blueprint

from .controllers import list_users, user_by_id

users = Blueprint('users', __name__)

base_url = '/users'

@users.route(f'{base_url}', methods=["GET"])
def get_users():
    return list_users()

@users.route(f'{base_url}/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    return user_by_id(user_id)
