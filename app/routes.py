from flask import jsonify
from app import api
from app.resources.todo import TodoList, Todo


@api.representation('application/json')
def output_json(data, code, headers=None):
    if 100 <= code < 400:
        resp = dict(data=data, success=True)
    else:
        resp = dict(error=data, success=False)

    resp = jsonify(resp)
    resp.headers.extend(headers or {})
    return resp


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
