from flask import Flask

from app.api.auth import SignupApi, LoginApi
from app.api.user import UserApi
from app.extensions import db, ma, api, bcrypt, jwt
from config.config import config


def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    initialize_routes(api)
    api.init_app(app)
    return None


def initialize_routes(api):
    api.add_resource(SignupApi, '/api/v1.0/auth/signup/')
    api.add_resource(LoginApi, '/api/v1.0/auth/login/')
    api.add_resource(UserApi, '/api/v1.0/user/')
    return None


app = create_app()
