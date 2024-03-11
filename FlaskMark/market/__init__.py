from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

app= Flask(__name__)    
file_path= os.path.abspath(os.getcwd())+"/instance/market.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+file_path

app.config['SECRET_KEY'] = '3e826f05ed1cebfb39fdaf66'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'market.db')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'FlaskMark', 'instance', 'market.db')


db= SQLAlchemy(app)
bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view= "login_page"
login_manager.login_message_category= "info"

from market import routes

