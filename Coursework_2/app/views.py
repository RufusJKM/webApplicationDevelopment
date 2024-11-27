from flask import render_template, flash, redirect, url_for, session
from app import app, db, models, admin
from flask_admin.contrib.sqla import ModelView
from .models import Product, Customer
from .forms import NewAccountForm, LoginForm, NewCardForm, ChooseCardForm, RatingForm, SearchForm, FilterForm

admin.add_view(ModelView(Product, db.session))
admin.add_view(ModelView(Customer, db.session))

def getName(item):
    return item.name

def getPrice(item):
    return item.price

def getRating(item):
    return item.rating

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
                    session['customer'] = customer.id
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
        # email and username must be unique
        for customer in models.Customer.query.all():
            if customer.email == form.email.data:
                error = True
                flash(f"Email already in use")
            elif customer.username == form.username.data:
                error = True
                flash(f"Username already in use")

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
            session['customer'] = c.id
            return redirect(url_for('home'))


    
    return render_template('signUp.html', title='Sign Up', form=form, error=error)

#Home view
@app.route('/home', methods=['GET', 'POST'])
def home():
    customerID = session['customer']
    customer = models.Customer.query.get(customerID)
    products = []
    for p in models.Product.query.all():
        products.append(p)
    form = FilterForm()
    error = False
    if form.validate_on_submit():
        #Alter product list based on filter
        if form.filterChoice.data != "None":
            products = []
            
            for p in models.Product.query.filter_by(category=form.filterChoice.data).all():
                products.append(p)
        #Otherwise keep the assessments list full
        else:
            products = []
            for p in models.Product.query.all():
                products.append(p)
        
        #Now sort using in-built sorted() function
        if (form.sortChoice.data == "Alphabetical"):
            products = sorted(products, key=getName)
        elif (form.sortChoice.data == "PLowHigh"):
            products = sorted(products, key=getPrice)
        elif (form.sortChoice.data == "PHighLow"):
            products = sorted(products, key=getPrice, reverse=True)
        else:
            products = sorted(products, key=getRating)


    return render_template('home.html', title='Home', customer=customer, products=products)

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