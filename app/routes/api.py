from flask import Blueprint

api_routes = Blueprint('api', __name__)


@api_routes.route('/auth/signup', methods=['POST'])
def signup():
    return {}, 201


@api_routes.route('/auth/login', methods=['POST'])
def login():
    return {'token': 'jdasf67iwy3thgfkdshjghy678i5gkhjnf'}, 200
