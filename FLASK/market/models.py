from market import db, login_manager
from flask_sqlalchemy import SQLAlchemy
from market import bcrypt
from flask_login import UserMixin
from datetime import datetime
import json


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#--------------------------------------------------------------------------------------------

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    PRN = db.Column(db.Integer(), nullable=False, unique=True)
    Password = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.Password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_passward):
        return bcrypt.check_password_hash(self.Password, attempted_passward)

    def __repr__(self):
        return f'User{self.name}'

#--------------------------------------------------------------------------------------------

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),nullable=False, unique=True)

    def __repr__(self):
        return f'Item{self.name}'

#--------------------------------------------------------------------------------------------

# Define a model for the orders table


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(length=30))
    order_id=db.Column(db.Integer, unique=True)
    Name=db.Column(db.String(length=30))
    quantity=db.Column(db.Integer,default=1)
    status=db.Column(db.String(20),default='pending',nullable=False)
    date=db.Column(db.DateTime,default=datetime.utcnow,nullable=False)
    

    def __repr__(self):
        return f'Order{self.order_id}'

#--------------------------------------------------------------------------------------------