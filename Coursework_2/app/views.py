from flask import render_template, flash, redirect, url_for, session, request
from app import app, db, models, admin
from flask_admin.contrib.sqla import ModelView
from .models import Product, Customer
from .forms import NewAccountForm, LoginForm, NewCardForm, ChooseCardForm, RatingForm, SearchForm, FilterForm, ProductForm

import json

def getName(item):
    return item.name

def getPrice(item):
    return item.price

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
        else:
            products = sorted(products, key=getPrice, reverse=True)
        
        


    return render_template('home.html', title='Home', customer=customer, products=products, form=form)

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
    customerID = session['customer']
    customer = models.Customer.query.get(customerID)
    numBaskets = 0
    for basket in customer.baskets:
        numBaskets+=1
    if numBaskets == 0:
        b = models.Basket(customer_id=customerID)
        db.session.add(b)
        db.session.commit()
        basketID = 1
    else:
        basketID = numBaskets

    basket = models.Basket.query.get(basketID)
    print(basketID)
    products = []

    #while quantity column doesn't work, i will store the quantities in a list instead
    quantities = []
    total = 0
    for basketproduct in basket.products:
        product = models.Product.query.get(basketproduct.product_id)
        products.append(product)
        quantities.append(5)
        #quantities.append(basketproduct.quantity)
        #total = total + product.price*basketproduct.quantity
    #print(quantities)

    return render_template('basket.html', title='Your Basket', products=products, quantities=quantities, total=total)

#View to add products to db
@app.route('/addProduct', methods=['GET', 'POST'])
def addProduct():
    error = False
    form = ProductForm()
    if form.validate_on_submit():
        for product in models.Product.query.all():
            if product.name == form.name.data:
                error = True
                flash(f"{form.name.data} is already in the database")

        if error == False:
            p = models.Product(name=form.name.data, imgurl=form.imgurl.data, category=form.category.data, price=form.price.data, count=form.count.data, rating=0)
            db.session.add(p)
            db.session.commit()
            flash(f"{form.name.data} added to the database")

    return render_template('admin.html', title='Admin', form=form, error=error)

#AJAX response views
@app.route('/changePrice', methods=['GET', 'POST'])
def changePrice():
    dictionary = json.loads(request.data)
    productID = int(dictionary["prodID"])
    product = models.Product.query.get(productID)
    return json.dumps({'status': 'OK', 'response': product.price })

@app.route('/addToBasket', methods=['GET', 'POST'])
def addToBasket():
    dictionary = json.loads(request.data)
    productID = int(dictionary["pID"])
    quantity = int(dictionary["quantity"])
    product = models.Product.query.get(productID)
    customerID = session['customer']
    customer = models.Customer.query.get(customerID)
    numBaskets = 0
    for basket in customer.baskets:
        numBaskets+=1
    if numBaskets == 0:
        b = models.Basket(customer_id=customerID)
        db.session.add(b)
        db.session.commit()
        basketID = 1
    else:
        basketID = numBaskets
        
    bp = models.BasketProducts(basket_id=basketID, product_id=productID, quantity=quantity)
    db.session.add(bp)
    db.session.commit()

    return json.dumps({'status': 'OK', 'response': productID })