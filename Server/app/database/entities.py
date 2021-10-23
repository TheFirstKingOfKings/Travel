from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)
ROLE_USER = 0


class User(db.Model):

    __tablename__ = 'user'

    id              = db.Column(db.Integer, index=True, primary_key=True)
    login           = db.Column(db.String(64), unique = True)
    password        = db.Column(db.String(120), unique = False)

    lastName        = db.Column(db.String(64), unique=False)
    email           = db.Column(db.String(120), unique = True)
    name            = db.Column(db.String(64), unique=False)

    age             = db.Column(db.Integer, unique=False)
    sex             = db.Column(db.Integer, unique=False)
    role            = db.Column(db.SmallInteger, default=ROLE_USER)
    routeId         = db.Column(db.Integer, index=True)
    interests       = db.Column(db.String, unique=False)


    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.login)


class Route(db.Model):
    __tablename__ = 'route'

    id              = db.Column(db.Integer, primary_key=True)
    length          = db.Column(db.Integer, unique=False)
    isPublic        = db.Column(db.Integer, unique=False)
    timeElapsed     = db.Column(db.Integer, unique=False)
