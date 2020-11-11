import os

from flask import Flask

from .database import db


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    from app.messenger.controllers import module
    app.register_blueprint(module)

    return app