from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
	firstName = StringField('First Name',validators=[DataRequired(),])
	lastName =StringField('Last Name',validators=[DataRequired(),])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Create Account')


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')

class RequestPickupForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(),Email()])
	storeName = StringField('Store Name', validators=[DataRequired()])
	orderNum = IntegerField('Order Number', validators=[DataRequired()])
	submit = SubmitField('Submit')

