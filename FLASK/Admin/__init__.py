from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY']='6f4f902b9e105e92f13fe5f6' # this will be get if you write in terminal python>>> import os>>> os.urandom(12).hex()
db = SQLAlchemy(app)
app.app_context().push()
bcrypt=Bcrypt(app)      # it convert the password into hash value
login_manager=LoginManager(app)
login_manager.login_view="login_page"
login_manager.login_message_category="info"

from Admin import route
