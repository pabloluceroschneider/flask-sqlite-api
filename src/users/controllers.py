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
        user = User.query.filter_by(id=user_id).first()
        return jsonify(user.toDict()), 200
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
    return jsonify(new_user.toDict()), 201

def update_user(user_id):
    data = request.get_json()
    user = User.query.filter_by(id=user_id).first()
    
    user.name = data["name"] 
    user.email = data["email"]
    user.address = data["address"]
    user.phone = data["phone"]

    db.session.commit()
    return jsonify(user.toDict()), 200

def remove_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({ "message": f"User {user.id} has been removed"}), 200