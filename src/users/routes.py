from flask import Blueprint

from .controllers import UserController

users = Blueprint('users', __name__)

base_url = '/users'

@users.route(f'{base_url}', methods=["POST"])
def create_user():
    return UserController.create_user()

@users.route(f'{base_url}', methods=["GET"])
def list_users():
    return UserController.list_users()

@users.route(f'{base_url}/<user_id>', methods=["GET"])
def user_by_id(user_id):
    return UserController.user_by_id(user_id)

@users.route(f'{base_url}/<user_id>', methods=["PUT"])
def update_user(user_id):
    return UserController.update_user(user_id)

@users.route(f'{base_url}/<user_id>', methods=["DELETE"])
def remove_user_by_id(user_id):
    return UserController.remove_user_by_id(user_id)
