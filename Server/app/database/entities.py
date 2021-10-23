from app import db

ROLE_USER = 0

class User(db.Model):

    id              = db.Column(db.Integer, primary_key = True)
    login           = db.Column(db.String(64), index = True, unique = True)
    password        = db.Column(db.String(120), index = True, unique = False)

    name            = db.Column(db.String(64), index=True, unique=False)
    lastName        = db.Column(db.String(64), index=True, unique=False)
    email           = db.Column(db.String(120), index = True, unique = True)

    age             = db.Column(db.Integer, index=True, unique=False)
    sex             = db.Column(db.Integer, index=True, unique=False)
    interests       = db.Column(db.String, index=True, unique=False)
    routeId         = db.Column(db.Integer)

    role            = db.Column(db.SmallInteger, default = ROLE_USER)

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<User {}>'.format(self.login)
