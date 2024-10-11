from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms import DecimalField
from wtforms.validators import DataRequired

class CalculatorForm(FlaskForm):
    number1 = IntegerField('number1', validators=[DataRequired()])
    number2 = IntegerField('number2', validators=[DataRequired()])

class PropertyForm(FlaskForm):
    address = StringField('Address', validators=[DataRequired()])
    duration = IntegerField('Duration', validators=[DataRequired()])
    rent = DecimalField('Rent', validators=[DataRequired()])
