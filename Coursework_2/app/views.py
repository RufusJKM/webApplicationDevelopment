from flask import render_template, flash, redirect, url_for
from app import app, db, models
from .forms import NewAccountForm, LoginForm, NewCardForm, ChooseCardForm, RatingForm, SearchForm



#Login Page
@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = False
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
                    currentUser = customer
                    return redirect(url_for('home'))
        
        print(f"Authenticate: {authenticate}\nfoundUser: {foundUser}")
        if authenticate == False:
            error = True
            flash(f"Username or password incorrect, to create a new account, click Sign Up")
    
    return render_template('login.html', title='login', form=form, error=error)

#Sign Up View
@app.route('/signUp', methods=['GET', 'POST'])
def signUp():
    length = False
    num = False
    uCase = False
    error = False
    form = NewAccountForm()
    if form.validate_on_submit():
        # email must be unique
        for customer in models.Customer.query.all():
            if customer.email == form.email.data:
                error = True
                flash(f"Email already in use")

        #ensure password meets required constraints
        password = form.password.data
        if len(password) >= 8:
            length = True
        for character in password:
            c = ord(character)
            if (c >= 48 and c <= 57):
                num = True
            elif (c >= 65 and c <= 90):
                uCase = True
        
        if length == False:
            error = True
            flash("Password must contain at least 8 characters")

        if num == False:
            error = True
            flash("Password must contain at least 1 number")

        if uCase == False:
            error = True
            flash("Password must contain at least 1 upper case letter")

        # add new customer after validation
        if error == False:
            c = models.Customer(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, username=form.username.data, password=form.password.data)
            db.session.add(c)
            db.session.commit()
            return redirect(url_for('home'))


    
    return render_template('signUp.html', title='Sign Up', form=form, error=error)

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