from flask import render_template, flash
from app import app, db, models
from .forms import NewAssessmentForm, FilterForm, ChooseForm

#Home view
@app.route('/', methods=['GET', 'POST'])
def home():
    #Passing in all the assessments in the database
    assessments = []
    for a in models.Assessment.query.all():
        assessments.append(a)
    form = FilterForm()
    if form.validate_on_submit():
        #If the user wishes to filter by either complete or incomplete, a new list of assessments is passed in
        if form.filterChoice.data == "True" or form.filterChoice.data == "False":
            assessments = []
            #Need to cast from String to Bool
            decision = bool(form.filterChoice.data)
            #List all assessments by the filter
            for a in models.Assessment.query.filter_by(completed=decision).all():
                assessments.append(a)
        #Otherwise keep the assessments list as it was

    return render_template('home.html', title='View Assessments', home=home, assessments=assessments, form=form)

#View for adding a new assessment
@app.route('/addNew', methods=['GET', 'POST'])
def addNew():
    form = NewAssessmentForm()
    if form.validate_on_submit():
        #Give the user positive feedback if the assessment gets added
        flash('Successfully added %s to assessments'%(form.title.data))
        
        #Add new assessment to the database 
        a = models.Assessment(title=form.title.data, module_code=form.code.data, deadline_date=form.dueDate.data, description=form.description.data, completed=form.completed.data)
        db.session.add(a)
        db.session.commit()
    addNew={'description':"Use the form below to add a new assessment to the data base, every field must have a value"}
    return render_template('addNew.html', title='Add Assessments', addNew=addNew, form=form)

#View for assessment editing
@app.route('/edit', methods=['GET', 'POST'])
def edit():
    assessments = []
    valid = False
    #For loop to get all assessments for display
    for a in models.Assessment.query.all():
        assessments.append(a)
    form = ChooseForm()
    if form.validate_on_submit():
        print("Validated")
        #For loop validating the users request against the database as the data is the assessment id
        for a in assessments:
            if form.chooseAssessment.data == a.id:
                valid = True
                break
        if valid == False:
            #Give negative feedback if the user enters something invalid
            flash("Please enter a number from the list of assessments above")

    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit, form=form, assessments=assessments, valid=valid)