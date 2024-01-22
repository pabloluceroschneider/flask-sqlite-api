from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

# app
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key constraints
@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
    if isinstance(dbapi_connection, SQLite3Connection):
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON;")
        cursor.close()


db = SQLAlchemy(app)
now = datetime.now()

# models
@dataclass
class User(db.Model):
    __tablename__ = "user"
    id: int
    name: str
    email: str
    address: str
    phone: str

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(50))
    posts = db.relationship("BlogPost", cascade="all, delete")

@dataclass
class BlogPost(db.Model):
    __tablename__ = "blog_post"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    body = db.Column(db.String(200))
    date = db.Column(db.Date)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

# routes
@app.route("/users", methods=["POST"])
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

@app.route("/users", methods=["GET"])
def get_all_users():
  users = User.query.all()
  return jsonify(users), 200

@app.route("/users/<user_id>", methods=["GET"])
def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user), 200

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return jsonify({}), 200