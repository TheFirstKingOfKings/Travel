# -*- coding: utf-8 -*-
import json

from app import app
from flask import request, redirect, g, session, flash

from app.database.entities import User
from app.forms.login import LoginForm
from app.processing.processing import Processing
from app.strs import setting


# LOG IN
@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def index():
    return redirect('/users/login/', 200)

# SIGN UP
@app.route('/signup', methods=['POST'])
def signup():
    logn = request.form['login']
    password = request.form['password']
    email = request.form['email']
    User.login = logn
    User.password = password
    User.email = email
    return logn


@app.route('/me/', methods=['POST'])
def homepage():
    return


@app.route('/users/login/', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    form = LoginForm(request.form)
    user = User.query.first()
    session['user_id'] = user.id
    flash('Welcome %s' % user.name)
    return redirect('/routes/', 200)


@app.route('/routes/', methods=['GET'])
def send_routes_available():
    data = json.loads(setting)
    processingAlgorhytm = Processing(data).process()
    return data[0]


@app.route('/routes/getRouteByParams', methods=['POST'])
def getRouteByParams():
    data = request.form
    print(data)
    processingAlgorhytm = Processing(data)
    return processingAlgorhytm.toStr()
