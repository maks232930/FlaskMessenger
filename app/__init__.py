from flask import Flask

from app import api
from app.api.routes import blueprint
from app.extensions import db
from app.extensions import login_manager
from config.config import config


def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(api.routes.blueprint)
    return None


app = create_app()
