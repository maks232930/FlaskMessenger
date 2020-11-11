import os


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = '2das41fsdf7sdfusFDFSE&&'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True