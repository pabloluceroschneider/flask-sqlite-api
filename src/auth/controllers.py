from flask import request, jsonify
from .services import AuthServices

def login():
    try:
        data = request.get_json()
        token = AuthServices.login(data)
        response = { "token": f"Bearer {token}" }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({ "error": e }), 500