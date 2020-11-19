from flask_sqlalchemy import SQLAlchemy
from app import create_app
import os


app = create_app()
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_POSTGRES')
db = SQLAlchemy(app)
