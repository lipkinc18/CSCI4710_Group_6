from flask import Flask, render_template, jsonify, json, redirect, request
import util
import os
from flask_sqlalchemy import SQLAlchemy


# current directory path
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'pickup2frontdoor.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(64))
    last_name= db.Column(db.String(64))
    email = db.Column(db.String(128))
    password = db.Column(db.String(64))

class Order(db.Model):
    _tablename_ = 'order'
    user_id = db.Column(db.Integer)
    order = db.Column(db.Integer)
    store = db.Column(db.String(64))
    pickup = db.Column(db.String(64))
    request_id = db.Column(db.Integer, primary_key=True)

class Pickup(db.Model):
    _tablename_ = 'pickup'
    user_id = db.Column(db.Integer)
    request = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer)
    cash = db.Column(db.Integer)


@app.route('/')
def index():
    # this is your index/homepage page
    db.drop_all()
    db.create_all()

    admin = User(id = 1, first_name = 'admin', last_name = 'admin', email = 'admin', password = 'password')
    db.session.add(admin)
    db.session.commit()
    print(User.query.all())

    log = 'homepage.'
    return render_template('index.html', log_index = log)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #this is your registration page
    log = 'register.'
    return render_template('register.html', log_request = log)

@app.route('/request')
def request():
    # this is your create a request page
    log = 'request.'
    return render_template('request.html', log_request = log)

@app.route('/accept')
def accept():
    # this is your accept a request page
    log = 'accept.'
    return render_template('accept.html', log_accept = log)

@app.route('/status')
def status():
    # this is your request status page
    log = 'status.'
    return render_template('status.html', log_status = log)

if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

