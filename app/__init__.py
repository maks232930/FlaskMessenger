from flask import Flask

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
    # api.add_resource()
    return None


app = create_app()
