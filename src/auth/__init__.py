from flask import Blueprint, request, jsonify

auth = Blueprint('auth', __name__)

base_url = '/auth'

@auth.route(f'{base_url}/issue', methods=["POST"])
def auth_get():
    try:
        user_data = request.get_json()
        return jsonify(user_data), 200
    except Exception as e:
        return jsonify({ "error": e }), 500

