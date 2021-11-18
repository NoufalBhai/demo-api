from flask import (
    Blueprint, request, jsonify
)
import sqlalchemy
from werkzeug.security import check_password_hash, generate_password_hash

from app.utlis import create_token
from app.schema import User
from app import db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    
    if not data:
        return {"error": "Please Provide Required Fields"}, 400
    email = data.get("email")
    password = data.get("password")
    if not email:
        return {"message": "Email is mandatory field"}, 400
    if not password:
        return {"message": "Password is mandatory field"}, 400

    password_hash = generate_password_hash(password)
    new_user = User(email=email, password=password_hash)
    try:
        db.session.add(new_user)
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        return {"error": "Email is Already Registered"}, 400
    db.session.refresh(new_user)
    user = {
        "email": new_user.email,
        "id": new_user.id
    }
    return jsonify(user), 201

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if not data:
        return {"error": "Please Provide Required Fields"}, 400
    email =data.get("email")
    password =data.get("password")
    if not email:
        return {"message": "Email is mandatory field"}, 400
    if not password:
        return {"message": "Password is mandatory field"}, 400
    user = User.query.filter(User.email==email).first()
    if not user:
        return { "error": f"User with email {email} is Not Found" }, 404
    if not check_password_hash(user.password, password):
        return { "error" : "Password or email Missmatch" }, 403
    user = {
        "id": user.id
    }
    token  = create_token(user)
    return jsonify({"access_token": token, "token_type": "baerer"}), 200
    