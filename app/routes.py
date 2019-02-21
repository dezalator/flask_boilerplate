from app import api
from app.resources.todo import TodoList, Todo

api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')
