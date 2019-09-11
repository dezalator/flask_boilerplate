from flask import json, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from flask_jwt_extended import (
    create_access_token, jwt_required, jwt_refresh_token_required, get_jwt_identity
)
from app.models.auth import User as UserModel
from app.common.utils import jwt_authorize


class Register(Resource):
    def post(self):
        data = json.loads(request.data)
        if UserModel.get_by_email(data['username']):
            raise Exception(f'User {data["username"]} already exists')
        if data['password'] != data['repeated_password']:
            raise Exception('Passwords do not match!')
        new_user = UserModel(
            username=data['username'],
            password=generate_password_hash(data['password'])
        )
        new_user.save()
        return jwt_authorize(new_user)


class User(Resource):
    @jwt_required
    def get(self, user_id):
        current_user = UserModel.query.filter_by(id=user_id).first()
        return current_user.to_dict()

    @jwt_required
    def put(self, user_id):
        pass


class UserLogin(Resource):
    def post(self):
        data = json.loads(request.data)
        current_user = UserModel.get_by_username(data['username'])
        if not current_user:
            raise Exception(f'User {data["username"]} not found')

        if check_password_hash(current_user.password, data['password']):
            return jwt_authorize(current_user)
        else:
            raise Exception(f'Wrong credentials')


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


class Secret(Resource):
    @jwt_required
    def get(self):
        return {
            'answer': 42
        }
