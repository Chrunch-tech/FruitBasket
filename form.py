""" Defining the forms used in this website in this file """
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import EmailField


class SearchFrom(FlaskForm):  # Search bar for the home page
    searchBar = StringField('', validators=[DataRequired(), Length(min=1)])
    search = SubmitField('Search')


class RegistrationForm(FlaskForm):  # For register the user's account
    username = StringField('Username: ', validators=[DataRequired(), Length(max=10)])
    email = EmailField('Email: ', validators=[DataRequired(), Length(max=50)])
    password = PasswordField("Password: ", validators=[DataRequired(), Length(min=8)])
    conform_password = PasswordField('Conform Password: ', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Submit')


class LoginForm(FlaskForm):  # For login the user with there account.
    username = StringField('Username: ', validators=[DataRequired(), Length(max=10)])
    password = PasswordField('Password: ', validators=[DataRequired(), Length(min=8)])
    sign_up = SubmitField('Sign up')


class Feedback(FlaskForm):  # For sending feedback.
    message_bar = StringField('', validators=[DataRequired(), Length(max=200)])
    send_button = SubmitField('Send')


class UpdateAccount(FlaskForm):  # To updating the  user account.
    name = StringField('Enter name:', validators=[DataRequired(), Length(max=10)])
    email = StringField('Enter email: ', validators=[DataRequired(), Length(max=20)])
    profile_img = FileField('Update profile image: ', validators=[FileAllowed(['jpg', 'png'])])
    update = SubmitField('Update')


class AddToCartForm(FlaskForm):
    amount = SelectField('', choices=['1kg', '2kg', '4kg', '6kg'])
    update_shipping = SubmitField('Add to cart')


class ShippingForm(FlaskForm):
    amount = SelectField('', choices=['1kg', '2kg', '4kg', '6kg'])
    check_out = SubmitField('Check out')
