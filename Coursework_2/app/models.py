from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    imgurl = db.Column(db.String(500))
    price = db.Column(db.Float)
    count = db.Column(db.Integer)
    orders = db.relationship('Order', backref='product', lazy='dynamic')

    def __repr__(self):
            return '{}{}{}{}{}'.format(self.id, self.name, self.imgurl, self.price, self.count)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    cards = db.relationship('Card', backref='customer', lazy='dynamic')
    orders = db.relationship('Order', backref='customer', lazy='dynamic')

    def __repr__(self):
            return '{}{}{}{}{}{}{}'.format(self.id, self.first_name, self.last_name, self.phone_number, self.email, self.username, self.password)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True)
    expirery = db.Column(db.DateTime)
    cvv = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

    def __repr__(self):
            return '{}{}{}{}'.format(self.id, self.number, self.expirery, self.cvv)

class Order(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

    def __repr__(self):
            return '{}{}'.format(self.customer_id, self.product_id)