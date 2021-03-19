import pymysql
pymysql.install_as_MySQLdb()
from flask import Flask, render_template, request, session, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.secret_key = 'super-secret-key'

@app.route("/")
def login():
    return render_template('login.html', params=params)

@app.route("/secret", methods=['GET', 'POST'])
def secret():

    if ('user' in session and session['user'] == params['admin_user']):
        return render_template('secret.html', params=params)


    if request.method=='POST':
        username = request.form.get('uname')
        userpass = request.form.get('pass')
        if (username == params['admin_user'] and userpass == params['admin_password']):
            #set the session variable
            session['user'] = username
            return render_template('secret.html', params=params)

    return render_template('login.html', params=params)

app.run(debug=True)