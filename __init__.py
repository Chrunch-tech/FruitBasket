""" Initializing this whole package """
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'MNIAAI13YO'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FruitBasket.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from . import routes
from . import model
