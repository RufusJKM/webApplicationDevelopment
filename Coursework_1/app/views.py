from flask import render_template, flash
from app import app, db, models
from .forms import NewAssessmentForm, FilterForm, ChooseForm

@app.route('/', methods=['GET', 'POST'])
def home():
    assessments = []
    for a in models.Assessment.query.all():
        assessments.append(a)
    form = FilterForm()
    if form.validate_on_submit():
        if form.filterChoice.data == "True" or form.filterChoice.data == "False":
            assessments = []
            decision = False
            if form.filterChoice.data == "True":
                decision = True
            else:
                decision = False
            for a in models.Assessment.query.filter_by(completed=decision).all():
                assessments.append(a)

    
    return render_template('home.html', title='View Assessments', home=home, assessments=assessments, form=form)

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
    assessments = []
    valid = False
    for a in models.Assessment.query.all():
        assessments.append(a)
    form = ChooseForm()
    if form.validate_on_submit():
        for a in assessments:
            print(form.chooseAssessment.data)
            if form.chooseAssessment.data == a.id:
                valid = True
                break
        if valid == False:
            flash("Please enter a number from the list of assessments above")

    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit, form=form, assessments=assessments, valid=valid)