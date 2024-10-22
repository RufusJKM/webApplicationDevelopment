from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms import StringField
from wtforms import BooleanField
from wtforms import DateField
from wtforms import RadioField
from wtforms import SelectField
from wtforms.validators import DataRequired
from app import app, db, models

#Form used to create a new assessment
class NewAssessmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    dueDate= DateField('Date', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    completed = BooleanField('Completed')

#Form used to filter results by complete/incomplete
class FilterForm(FlaskForm):
    filterChoice = SelectField(u'Filter by ', choices=[('True', 'Complete'), ('False', 'Incomplete'), ('Null', 'No Filter')], validators=[DataRequired()])

#Form used to pick an assessment to change
class ChooseForm(FlaskForm):
    chooseAssessment = IntegerField('chooseAssessment', validators=[DataRequired()])
    
#Form to change details of an assessment
class EditForm(FlaskForm):
    title = StringField('Title')
    code = IntegerField('Code')
    dueDate= DateField('Date')
    description = StringField('Description')
    completed = BooleanField('Completed')