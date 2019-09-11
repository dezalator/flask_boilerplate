from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from app.config import Config
from app.common.api import BaseApi


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = BaseApi(app)
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


from app import routes
