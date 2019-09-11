from flask_jwt_extended import create_access_token, create_refresh_token


def jwt_authorize(user):
    access_token = create_access_token(user.username)
    refresh_token = create_refresh_token(user.username)
    return {
        'id': user.id,
        'access_token': access_token,
        'refresh_token': refresh_token
    }
