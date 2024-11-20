from flask import render_template, flash, redirect, url_for
from app import app, db, models

#Home view
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')

#Account details view
@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account.html', title='Your Account')

#Basket view
@app.route('/prevOrders', methods=['GET', 'POST'])
def prevOrders():
    return render_template('prevOrders.html', title='Your Orders')

#Basket view
@app.route('/basket', methods=['GET', 'POST'])
def basket():
    return render_template('basket.html', title='Your Basket')