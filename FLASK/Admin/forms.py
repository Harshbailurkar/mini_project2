from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,validators,ValidationError,TextAreaField
from wtforms.validators import Length,EqualTo,Email,DataRequired
from Admin.models import Admin

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
    