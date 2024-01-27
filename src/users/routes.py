from flask import Blueprint

from .controllers import list_users, user_by_id, create_user

users = Blueprint('users', __name__)

base_url = '/users'

@users.route(f'{base_url}', methods=["POST"])
def post_create_user():
    return create_user()

@users.route(f'{base_url}', methods=["GET"])
def get_list_users():
    return list_users()

@users.route(f'{base_url}/<user_id>', methods=["GET"])
def get_user_by_id(user_id):
    return user_by_id(user_id)
