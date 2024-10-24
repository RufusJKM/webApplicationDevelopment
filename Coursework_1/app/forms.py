from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, BooleanField, DateField, SelectField
from wtforms.validators import DataRequired
from app import app, db, models

#Form used to create a new assessment
#Reference for render_kw: Stack Overflow. [Online]. [Accessed 24/10/2024]. Available from https://stackoverflow.com/questions/64820785/can-you-adjust-the-width-of-a-question-in-flask-wtforms
class NewAssessmentForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    dueDate= DateField('Date', validators=[DataRequired()])
    description = StringField('Description', render_kw={'size': 60}, validators=[DataRequired()])
    completed = BooleanField('Completed')

#Form used to filter results by complete/incomplete
class FilterForm(FlaskForm):
    filterChoice = SelectField(u'Filter by ', choices=[('None', 'No Filter'), ('True', 'Complete'), ('False', 'Incomplete')], validators=[DataRequired()])

#Form used to pick an assessment to change
class ChooseForm(FlaskForm):
    chooseAssessment = IntegerField('chooseAssessment', validators=[DataRequired()])
    
#Form to change details of an assessment
class EditForm(FlaskForm):
    #The hidden field is used to hold the id of the chosen assessment
    hidden = IntegerField('Hidden', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    code = IntegerField('Code', validators=[DataRequired()])
    dueDate= DateField('Date', validators=[DataRequired()])
    description = StringField('Description', render_kw={'size': 60}, validators=[DataRequired()])
    completed = BooleanField('Completed')