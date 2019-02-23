from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.resources.todo import Todo, TodoList
from app.config import Config
from app.common.api import BaseApi


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app)
api = BaseApi(app)

from app import routes