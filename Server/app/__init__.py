from flask import Flask
from config import Config

basedir = './'

app = Flask(__name__)
app.config.from_object(Config)


from app import routes
from app.database import entities
