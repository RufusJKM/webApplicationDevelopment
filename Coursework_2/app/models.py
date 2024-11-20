from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), index=True, unique=True)
    imgurl = db.Column(db.String(500))
    category = db.Column(db.String(50))
    price = db.Column(db.Float)
    count = db.Column(db.Integer)

    def __repr__(self):
            return '{}{}{}{}{}'.format(self.id, self.name, self.imgurl, self.category, self.price, self.count)

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), index=True)
    last_name = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(50))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __repr__(self):
            return '{}{}{}{}{}{}{}'.format(self.id, self.first_name, self.last_name, self.phone_number, self.email, self.username, self.password)

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, index=True, unique=True)
    expirery = db.Column(db.DateTime)
    cvv = db.Column(db.Integer)

    def __repr__(self):
            return '{}{}{}{}'.format(self.id, self.number, self.expirery, self.cvv)

class Basket(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)

    def __repr__(self): 
            return '{}{}'.format(self.customer_id, self.product_id)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self): 
            return '{}'.format(self.id)