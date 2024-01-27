from flask import request, jsonify
from .models import User
from .. import db

def list_users():
    try:
        users = User.query.all()
        print(users)
        response = []
        for user in users: response.append(user.toDict())
        return jsonify(response)
    except Exception as e:
        return jsonify({ "error": e }), 500
    
def user_by_id(user_id):
    try:
        return jsonify({ "id": user_id}), 200
    except Exception as e:
        return jsonify({ "error": e }), 500
    
def create_user():
    data = request.get_json()
    new_user = User(
      name=data["name"],
      email=data["email"],
      address=data["address"],
      phone=data["phone"],
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"messager": "user created"}), 200