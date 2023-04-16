import json
import re
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from sqlalchemy import or_, and_
from config import Regexp
from dtos.user_dto import UserSignUpDTO, UserLogInDTO
from models.user import User
from models.database import database

api_routes = Blueprint('api', __name__)

passValid = re.compile(Regexp.PASSWORD)
mailValid = re.compile(Regexp.EMAIL)


@api_routes.route('/auth/signup', methods=['POST'])
def signup():
    try:
        user = json.loads(request.data, object_hook=UserSignUpDTO.from_json)

        if not mailValid.match(user.email):
            return {"error": "invalid email"}, 400

        if user.password1 != user.password2:
            return {"error": "password1 and password2 must be equals"}, 400

        if not passValid.match(user.password1):
            return {
                "error": "invalid password, check: size between 6-20 characters, have at least one Uppercase and "
                         "Lowercase letter, at least one number and at least one special character"}, 400

        if User.query.filter(or_(User.username == user.username, User.email == user.email)).first() is not None:
            return {"error": "user or email already exist"}, 400

        new_user = User(username=user.username, password=user.password1, email=user.email)
        database.session.add(new_user)
        database.session.commit()
        return {}, 201
    except KeyError:
        return {"error": "Bad request"}, 400


@api_routes.route('/auth/login', methods=['POST'])
def login():
    try:
        user_request = json.loads(request.data, object_hook=UserLogInDTO.from_json)
        user_db = User.query.filter(and_(or_(User.username == user_request.username, User.email == user_request.username),
                                    User.password == user_request.password)).first()
        if user_db is not None:
            token = create_access_token(identity=user_db.id)
            return {"message": "successful login", "token": token, "id": user_db.id}, 200

        return {"error", "invalid credentials"}, 400

    except KeyError:
        return {"error": "Bad request"}, 400
