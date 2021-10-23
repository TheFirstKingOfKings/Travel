from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    login           = TextField('name', [Required()])
    email           = TextField('Email address', [Required(), Email()])
    password        = PasswordField('Password', [Required()])
    confirm         = PasswordField('Repeat Password', [
                        Required(),
                        EqualTo('password', message='Passwords must match')
                    ])