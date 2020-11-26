import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    CSRF_ENABLED = True
    TESTING = True
    SECRET_KEY = '312h1ib31BJKB*&^&*Sdasdw'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost/messenger'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
