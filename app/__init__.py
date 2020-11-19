from flask import Flask
# from flask_migrate import Migrate
from config.config import config


def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])
    from app.main.routers import main

    app.register_blueprint(main)
    return app

# migrate = Migrate(app, db)
