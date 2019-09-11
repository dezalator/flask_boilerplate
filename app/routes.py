from flask import jsonify
from app import api
from app.resources.auth import User, Register, UserLogin, TokenRefresh, Secret


@api.representation('application/json')
def output_json(data, code, headers=None):
    if 100 <= code < 400:
        resp = dict(data=data, success=True)
    else:
        resp = dict(error=data, success=False)

    resp = jsonify(resp)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(Register, '/register/')
api.add_resource(UserLogin, '/login/')
api.add_resource(User, '/user/<user_id>/')
api.add_resource(TokenRefresh, '/token/')
api.add_resource(Secret, '/secret/')
