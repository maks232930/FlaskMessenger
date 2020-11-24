from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from config.config import config


def create_app(app_config='development'):
    app = Flask(__name__)
    app.config.from_object(config[app_config])

    return app


app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
