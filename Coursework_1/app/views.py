from flask import render_template, flash, request
from app import app, db, models
from .forms import NewAssessmentForm, FilterForm, ChooseForm, EditForm

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
    newName = True
    if form.validate_on_submit():
        for a in assessments:
                if form.title.data == a.title:
                    #Give the user negative feedback so they know their request didn't work
                    flash("An assessment with the name {a.title} already exists")
                    newName = False
        if newName == True:
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
    
    form1 = ChooseForm()
    form2 = EditForm()
    chosenAssessment = None
    newName = True

    if form1.validate_on_submit():
        #For loop validating the users request against the database as the data is the assessment id
        for a in assessments:
            if form1.chooseAssessment.data == a.id:
                valid = True
                chosenAssessment =  models.Assessment.query.get(form1.chooseAssessment.data)
                break
        if valid == False:
            #Give negative feedback if the user enters something invalid
            flash("Please enter a number from the list of assessments above")
    
    elif form2.validate_on_submit():

        assessment_id = request.form["assessment_id"]
        print(assessment_id)
        chosenAssessment = models.Assessment.query.get(int(assessment_id))
        #Change title if necessary
        print(form2.title.data)
        print(form2.code.data)
        print(form2.dueDate.data)
        print(form2.description.data)
        print(form2.completed.data)
        if (form2.title.data != None):
            #Must still be a unique name
            for a in assessments:
                if form2.title.data == a.title:
                    flash(f"An assessment with the name {a.title} already exists")
                    newName = False
        
            if newName == True:  
                chosenAssessment.title =  form2.title.data
                db.session.commit()
        
        #change course code if necessary 
        if (form2.code.data != None):
            chosenAssessment.module_code = form2.code.data
            db.session.commit()

        #change dealine date if necessary
        if (form2.dueDate.data != None):
            chosenAssessment.deadline_date = form2.dueDate.data
            db.session.commit()

        #change description if necessary
        if (form2.description.data != None):
            chosenAssessment.description = form2.description.data
            db.session.commit()
        
        #Completed will always have either true or false in data
        chosenAssessment.completed = form2.completed.data
        db.session.commit()

                


    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit, ChooseForm=form1, EditForm=form2, assessments=assessments, valid=valid, chosenAssessment=chosenAssessment)