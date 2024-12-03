from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, DateField, SelectField, PasswordField, EmailField, RadioField, DecimalField
from wtforms.validators import DataRequired
from app import app, db, models

class NewAccountForm(FlaskForm):
    first_name = StringField('FName', validators=[DataRequired()])
    last_name = StringField('LName', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('UName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class LoginForm(FlaskForm):
    username = StringField('UName', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class NewCardForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired()])
    expiry = DateField('Expiry', validators=[DataRequired()])
    cvv = IntegerField('CVV', validators=[DataRequired()])

#Dynamic radio button to choose payment method
class ChooseCardForm(FlaskForm):
    option = RadioField('Option', choices=[])

class RatingForm(FlaskForm):
    rating = RadioField('Rating', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], validators=[DataRequired()])
    comment = StringField('Comment')

class SearchForm(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])

class FilterForm(FlaskForm):
     filterChoice = SelectField(u'Filter by ', choices=[('None', 'No Filter'), ('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'),  ('Meats', 'Meats')], validators=[DataRequired()])
     sortChoice = SelectField(u'Sort by ', choices=[('Alphabetical', 'A-Z'), ('PLowHigh', 'Price Low to High'), ('PHighLow', 'Price High to Low')], validators=[DataRequired()])

class ProductForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    imgurl = StringField('imgurl', validators=[DataRequired()])
    category = SelectField(u'Category', choices=[('Vegetables', 'Vegetables'), ('Fruits', 'Fruits'),  ('Meats', 'Meats')], validators=[DataRequired()])
    price = DecimalField('price', validators=[DataRequired()])
    count = IntegerField('count', validators=[DataRequired()])