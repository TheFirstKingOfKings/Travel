import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join('database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_MIGRATE_REPO = os.path.join(basedfir, 'db_repository')