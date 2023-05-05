from market import app
from flask import render_template, redirect, url_for, flash, request, session,jsonify
from market.models import Item, User, Orders
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user
import uuid
from datetime import datetime
import secrets
from bs4 import BeautifulSoup
import requests
import json

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

#---------------------------------------------------------------------------------------------------

@app.route('/menu', methods=['GET', 'POST'])

def Menu_page():
    items = Item.query.all()
    return render_template('Menu.html', items=items)

#---------------------------------------------------------------------------------------------------

@app.route('/Profile', methods=['GET', 'POST'])
@login_required
def profile_page():
    return render_template('profile.html')

#---------------------------------------------------------------------------------------------------

@app.route('/Order history', methods=['GET', 'POST'])
@login_required
def history_page():
    return render_template('history.html')

#---------------------------------------------------------------------------------------------------

@app.route('/setting', methods=['GET', 'POST'])
@login_required
def setting_page():
    return render_template('setting.html')

#---------------------------------------------------------------------------------------------------

@app.route('/Wallet', methods=['GET', 'POST'])
@login_required
def wallet_page():
    return render_template('Wallet.html')

#---------------------------------------------------------------------------------------------------

@ app.route('/About' )
@login_required
def about_page():
    return render_template('About.html')

#---------------------------------------------------------------------------------------------------

@app.route('/menu', methods=['GET', 'POST'])
@login_required
def selected_items():
    
    # Retrieve the selected items array from the session
    selectedItems = session.get('selectedItems', [])
    # Render the selected items template with the array data
    return render_template('Menu.html', selectedItems=selectedItems)

#---------------------------------------------------------------------------------------------------

@app.route('/success', methods=['GET', 'POST'])
@login_required
def success_page():
    return render_template('success.html')

#---------------------------------------------------------------------------------------------------

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              PRN=form.PRN.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(
            f'Account Created Successfully! You are logged in as: {user_to_create.username}', category='success')

        return redirect(url_for('Menu_page'))
    if form.errors != {}:  # If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(
                f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

#---------------------------------------------------------------------------------------------------

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(
            username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_passward=form.password.data
        ):
            login_user(attempted_user)
            flash(
                f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('Menu_page'))
        else:
            flash('Username and password are not match! Please try again',
                  category='danger')

    return render_template('login.html', form=form)

#---------------------------------------------------------------------------------------------------

@app.route('/logout')
@login_required
def logout_page():
    logout_user()
    flash("You have been logged Out", category='info')
    return redirect(url_for('home_page'))

#---------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------


@app.route('/submit', methods=['GET','POST'])
@login_required
def submit_order():
    # get the order data from the request
    order_data = request.get_json()

    # parse the order data to get the table data
    table_data = order_data['table_data']

    # save the order in the database
    username = current_user.username
    order_id = secrets.token_hex(2)
    try:
        order = Orders(username=username, order_id=order_id, orders=json.dumps(table_data))
        db.session.add(order)
        db.session.commit()
        return jsonify({'success': True, 'order_id': order_id})
    except Exception as e:
        print(e)
        return jsonify({'success': False, 'message': 'Something went wrong while you order'})

@app.route('/success/<order_id>')
@login_required
def success_page(order_id):
    return render_template('success.html', order_id=order_id)

