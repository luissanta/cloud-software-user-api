import json

from flask import Blueprint, request
from flask_jwt_extended import create_access_token

from dtos.user_dto import UserDTO
from models.user import User
from models.database import database

api_routes = Blueprint('api', __name__)


@api_routes.route('/auth/signup', methods=['POST'])
def signup():
    try:
        user = json.loads(request.data, object_hook=UserDTO.from_json)
        if User.query.filter(User.username == user.username).first() is not None:
            return {"error": "user already exist"}, 400

        newUser = User(username=user.username, password=user.password)
        database.session.add(newUser)
        database.session.commit()
        return {}, 201
    except KeyError:
        return {"error": "Bad request"}, 400

@api_routes.route('/auth/login', methods=['POST'])
def login():
    try:
        user_request = json.loads(request.data, object_hook=UserDTO.from_json)
        user_db = User.query.filter(User.username == user_request.username, User.password == user_request.password).first()
        if user_db is not None:
            additional_claims = {"id": user_db.id}
            token_de_acceso = create_access_token(identity=user_db.id, additional_claims=additional_claims)
            return {"message": "successful login", "token": token_de_acceso, "id": user_db.id}, 200

        return {"error", "invalid credentials"}, 400

    except KeyError:
        return {"error": "Bad request"}, 400
