from Admin import db, login_manager
from Admin import bcrypt
from flask_login import UserMixin
from datetime import datetime


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))

#---------------------------------------------------------------------------------------------------

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
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



