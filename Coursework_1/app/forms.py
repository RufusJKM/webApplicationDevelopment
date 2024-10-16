from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms import BooleanField
from wtforms import DateField
from wtforms import RadioField
from wtforms import SelectField
from wtforms.validators import DataRequired

class NewAssessmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    dueDate= DateField('Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    completed = BooleanField('Completed')

class FilterForm(FlaskForm):
    filterChoice = SelectField(u'Filter by ', choices=[('True', 'Complete'), ('False', 'Incomplete'), ('Null', 'No Filter')], validators=[DataRequired()])