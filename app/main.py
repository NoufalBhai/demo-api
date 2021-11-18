from os import error
from flask import (
    Blueprint, request
)
from app.schema import Profile
from app import db
from datetime import date
from app.utlis import verify_token

bp = Blueprint("main", __name__, url_prefix="/")



@bp.route("/profile", methods=("POST",))
def create_profile():
    bearer_token = request.headers.get("Authorization")
    if not bearer_token:
        return {"error": "Provide a valid authentiaction token"} , 401
    token = bearer_token.split(" ")[-1]
    data, error = verify_token(token)
    if error:
        return {"error": "Invalid Token"}, 403
    
    user_id = data.get("id")
    data = request.json
    print(request.headers)
    if not data:
        return {"error": "Please Provide mandatory Fields"}, 400
    name = data.get("name")
    gender = data.get("gender")
    dob = data.get("dob")
    if not name:
        return {"error": "name is a mandatory field"}, 400
    if not gender:
        return {"error": "gender is a mandatory field"}, 400
    if not dob:
        return {"error": "dob is a mandatory field"}, 400
    if dob:
        dob = date.fromisoformat(dob)
    profile = db.session.query(Profile).filter(Profile.user_id == user_id).first()
    if profile:
        return {"message": "Profile Already Existed"}, 200
    profile = Profile(name=name, dob=dob, gender=gender, user_id=user_id)
    db.session.add(profile)
    db.session.commit()
    db.session.refresh(profile)
    return {"id": profile.id,  "name": profile.name, "gender": profile.gender, "dob": profile.dob}, 201
           

@bp.route("/profile", methods=("PUT",))
def update_profile():
    
    bearer_token = request.headers.get("Authorization")
    if not bearer_token:
        return {"error": "Provide a valid authentiaction token"} , 401
    token = bearer_token.split(" ")[-1]
    data, error = verify_token(token)
    if error:
        return {"error": "Invalid Token"}, 403
    
    user_id = data.get("id")
    data = request.json
    if not data:
        return {"error": "Please Provide mandatory Fields"}, 400
    name = data.get("name")
    gender = data.get("gender")
    dob = data.get("dob")
    if not name:
        return {"error": "name is a mandatory field"}
    if not gender:
        return {"error": "gender is a mandatory field"}
    if not dob:
        return {"error": "dob is a mandatory field"}
    if dob:
        dob = date.fromisoformat(dob)
    profile = db.session.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        return {"error": "No Profile found"}, 404
    
    profile.name = name
    profile.dob = dob
    profile.gender = gender
    db.session.commit()
    db.session.refresh(profile)
    return {"id": profile.id,  "name": profile.name, "gender": profile.gender, "dob": profile.dob}, 200

