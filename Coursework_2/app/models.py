from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    imgurl = db.Column(db.String(500))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    count = db.Column(db.Integer)
    basket_id = db.Column(db.Integer, db.ForeignKey('basket.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))

    def __repr__(self):
            return '{}{}{}{}{}'.format(self.id, self.name, self.imgurl, self.category, self.price, self.count)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), index=True)
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    cards = db.relationship('Card', backref='customer', lazy='dynamic')
    basket = db.relationship('Basket', backref='customer', lazy='dynamic')


    def __repr__(self):
            return '{}{}{}{}{}{}{}'.format(self.id, self.first_name, self.last_name, self.phone_number, self.email, self.username, self.password)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)
    expiry = db.Column(db.DateTime)
    cvv = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
            return '{}{}{}{}'.format(self.id, self.number, self.expirery, self.cvv)

class Basket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    products = db.relationship('Product', backref='basket', lazy='dynamic')

    def __repr__(self): 
            return '{}{}'.format(self.id, self.customer_id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    products = db.relationship('Product', backref='order', lazy='dynamic')

    def __repr__(self): 
            return '{}{}'.format(self.id, self.customer_id)