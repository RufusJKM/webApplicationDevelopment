from flask import render_template, flash
from app import app, db, models
from .forms import NewAssessmentForm

@app.route('/', methods=['GET', 'POST'])
def home():
    assessments = []
    for a in models.Assessment.query.all():
        assessments.append(a)
    home={'description':"Use this page to view all assessments, filter by completion and view assessment details"}
    return render_template('home.html', title='View Assessments', home=home, assessments=assessments)

@app.route('/addNew', methods=['GET', 'POST'])
def addNew():
    form = NewAssessmentForm()
    if form.validate_on_submit():
        flash('Successfully added %s to assessments'%(form.title.data))
        a = models.Assessment(title=form.title.data, module_code=form.code.data, deadline_date=form.dueDate.data, description=form.description.data, completed=form.completed.data)
        db.session.add(a)
        db.session.commit()
    addNew={'description':"Use the form below to add a new assessment to the data base, every field must have a value"}
    return render_template('addNew.html', title='Add Assessments', addNew=addNew, form=form)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit)