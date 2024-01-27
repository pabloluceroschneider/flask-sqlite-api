from flask import Blueprint, request, jsonify

users = Blueprint('users', __name__)

base_url = '/users'

@users.route(f'{base_url}/issue', methods=["GET"])
def users_get():
    try:
        user_data = request.get_json()
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({ "error": e }), 500

