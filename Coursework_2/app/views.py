from flask import render_template, flash, redirect, url_for
from app import app, db, models
from .forms import NewAccountForm, LoginForm, NewCardForm, ChooseCardForm, RatingForm, SearchForm

#Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    foundUser = False
    authenticate = False
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        for customer in models.Customer.query.all():
            if customer.username == username:
                foundUser = True
                if customer.password == password:
                    authenticate = True
                    #switch to home page
        
        print(f"Authenticate: {authenticate}\nfoundUser: {foundUser}")
        if authenticate == False:
            flash(f"Username or password incorrect, to create a new account, click Sign Up")
    
    return render_template('login.html', title='login', form=form)

#Home view
@app.route('/home', methods=['GET', 'POST'])
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