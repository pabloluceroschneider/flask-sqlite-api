from flask import request, jsonify
from .models import User
from .. import db

class UserController:
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
        try:
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
        except Exception as e:
            return jsonify({ "error": e }), 500

    def update_user(user_id):
        try:
            data = request.get_json()
            user = User.query.filter_by(id=user_id).first()

            user.name = data["name"] 
            user.email = data["email"]
            user.address = data["address"]
            user.phone = data["phone"]

            db.session.commit()
            return jsonify(user.toDict()), 200
        except Exception as e:
            return jsonify({ "error": e }), 500

    def remove_user_by_id(user_id):
        try:
            user = User.query.filter_by(id=user_id).first()
            db.session.delete(user)
            db.session.commit()
            return jsonify({ "message": f"User with id '{user.id}' has been successfully removed"}), 200
        except Exception as e:
            return jsonify({ "error": e }), 500
