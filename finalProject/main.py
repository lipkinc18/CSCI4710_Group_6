from flask import Flask, render_template, jsonify, json, redirect, request, flash, url_for
import util
import os
from flask_sqlalchemy import SQLAlchemy
from forms import RegisterForm, LoginForm, RequestPickupForm
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user,logout_user, current_user

app = Flask(__name__)

app.config['SECRET_KEY']= "Guess my key!"
# current directory path
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
'sqlite:///' + os.path.join(basedir, 'pickup2frontdoor.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    _tablename_ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String(64))
    last_name= db.Column(db.String(64))
    email = db.Column(db.String(128),)
    password = db.Column(db.String(64))

    def __repr__(self):
        return f"User('{self.first_name}','{self.email}')"

class Order(db.Model):
    _tablename_ = 'order'
    id = db.Column(db.Integer, primary_key=True)
    order = db.Column(db.Integer)
    store = db.Column(db.String(64))
    pickup_status = db.Column(db.String(64))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Order('{self.order}','{self.store}')"

class Pickup(db.Model):
    _tablename_ = 'pickup'
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.Integer)
    store = db.Column(db.String(64))
    status = db.Column(db.String(64))
    cash = db.Column(db.Integer)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return f"Pickup('{self.store},{self.request}','{self.status}','{self.cash})"


@app.route('/')
def index():
    # this is your index/homepage page
    db.drop_all()
    db.create_all()

    admin = User(first_name = 'admin', last_name = 'admin', email = 'admin@admin.com', password = 'password')
    lowes = Pickup(request = 4721, store = 'Lowes', status = 'Pending', cash = 5, user_id = 'admin@amin.com')
    walmart = Pickup(request = 1274, store = 'Walmart', status = 'Pending', cash = 5, user_id = 'admin@amin.com')
    target = Pickup(request = 2741, store = 'Target', status = 'Pending', cash = 5, user_id = 'admin@amin.com')
    lo = Order(order = 4721, store = 'Lowes', pickup_status = 'Pending', user_id = 'admin@amin.com')
    wa = Order(order = 1274, store = 'Walmart', pickup_status = 'Pending', user_id = 'admin@amin.com')
    ta = Order(order = 2741, store = 'Target', pickup_status = 'Pending', user_id = 'admin@amin.com')
    db.session.add(admin)
    db.session.add_all([lowes, walmart, target])
    db.session.add_all([lo, wa, ta])
    db.session.commit()

    log = 'homepage.'
    return render_template('index.html', log_index = log)

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user= User(first_name = form.firstName.data, last_name = form.lastName.data , email = form.email.data , password = hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title="register", form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('request'))
    return render_template('login.html', title="register", form=form)


@app.route('/request', methods=['GET','POST'])
def request():
    form= RequestPickupForm()
    if form.validate_on_submit():
        orderRequest = Order(order= form.orderNum.data, store= form.storeName.data, pickup_status="Pending", user_id=form.email.data)
        pickup = Pickup(request= form.orderNum.data,store =form.storeName.data, status= 'Pending', cash= 5,user_id=form.email.data )
        db.session.add(orderRequest)
        db.session.add(pickup)
        db.session.commit()
        return redirect(url_for('status'))
    return render_template('request.html', title="requestPickupForm", form=form)

@app.route('/accept')
def accept():
    pickups = Pickup.query.all()
    return render_template('accept.html', pickups = pickups,log_html=Pickup.query.all())

@app.route('/status')
def status():
    status = Order.query.all()
    print(status)
    payment= 5
    print(payment)
    completed = Pickup.query.filter_by(status = 'Completed').count()
    return render_template('status.html', status=status, payment=payment, completed=completed)


@app.route('/get_pickup', methods=['GET'])
def get_pickup():
    print(Pickup.query.all())
    return util.parse_pickup(Pickup.query.all())

@app.route('/accept_pickup/<selected_pick>',methods=['MY_PICK'])
def accept_pick(selected_pick = ''):
    Pickup.query.filter(Pickup.store==selected_pick).update(dict(status= 'Completed'))
    Order.query.filter(Order.store==selected_pick).update(dict(pickup_status= 'Completed'))
    db.session.commit()
    print(Pickup.query.all())
    return 'pickup completed'


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.debug = True
    ip = '127.0.0.1'
    app.run(host=ip)

