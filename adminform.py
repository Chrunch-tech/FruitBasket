""" Defining the admin forms used in this website in this file """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length


class AdminForm(FlaskForm):  # Form to authenticate the admins
    adminId = StringField("Admin Id:", validators=[DataRequired(), Length(max=20)])
    adminName = StringField("Admin Name:", validators=[DataRequired(), Length(max=7)])
    password = PasswordField('Password:', validators=[DataRequired(), Length(min=8)])
    sign_in = SubmitField("Sign up")


class AddProduct(FlaskForm):  # Form for add products
    productId = StringField('Product Id:', validators=[DataRequired(), Length(max=10)])
    productName = StringField('Product Name:', validators=[DataRequired(), Length(max=20)])
    price = IntegerField('Price:', validators=[DataRequired()])
    stock = IntegerField('Stock:', validators=[DataRequired()])
    description = StringField('Description: ', validators=[DataRequired(), Length(max=20)])
    image_url = StringField('Image url:', validators=[DataRequired(), Length(max=255)])
    post = SubmitField('Post')
