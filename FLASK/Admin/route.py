from Admin import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages, request, session
from Admin.forms import LoginForm
from Admin import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    
    form = LoginForm()
    if form.validate_on_submit():
        attempted_admin =form.username.data
        if attempted_admin and attempted_admin.check_password_correction(
                attempted_passward=form.password.data
        ):
            login_user(attempted_admin)
            flash(
                f'Success! You are logged in as: {attempted_admin.username}', category='success')
            return redirect(url_for('Menu_page'))
        else:
            flash('Username and password are not match! Please try again',
                  category='danger')

    return render_template('login.html', form=form)
