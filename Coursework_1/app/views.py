from flask import render_template, flash, redirect, url_for
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
            
            #Need to convert from String to Bool
            if form.filterChoice.data == "True":
                decision = True
            else:
                decision = False

            #Create new list of assessments
            for a in models.Assessment.query.filter_by(completed=decision).all():
                assessments.append(a)
        #Otherwise keep the assessments list as it was

    return render_template('home.html', title='View Assessments', home=home, assessments=assessments, form=form)

#View for adding a new assessment
@app.route('/addNew', methods=['GET', 'POST'])
def addNew():
    form = NewAssessmentForm()
    newName = True
    assessments = []
    for a in models.Assessment.query.all():
        assessments.append(a)
    if form.validate_on_submit():
        for a in assessments:
                if form.title.data == a.title:
                    #Give the user negative feedback so they know their request didn't work
                    flash(f"An assessment with the name {a.title} already exists")
                    newName = False
        if newName == True:
            #Give the user positive feedback if the assessment gets added
            flash(f'Successfully added {form.title.data} to assessments')
            
            #Add new assessment to the database 
            a = models.Assessment(title=form.title.data, module_code=form.code.data, deadline_date=form.dueDate.data, description=form.description.data, completed=form.completed.data)
            db.session.add(a)
            db.session.commit()
            #Refresh the page after submission
            #Reference: Stack Overflow. [Online]. [Accessed 23/10/2024]. Available from https://stackoverflow.com/questions/31945329/clear-valid-form-after-it-is-submitted
            return redirect(url_for('addNew'))

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
                #Have to set value here as it doesn't populate properly through html
                form2.completed.data = chosenAssessment.completed
                break
        if valid == False:
            #Give negative feedback if the user enters something invalid
            flash("Please enter a number from the list of assessments above")
    
    elif form2.validate_on_submit():
        #Get chosenAssessment
        changed = False
        assessment_id = form2.hidden.data
        chosenAssessment = models.Assessment.query.get(assessment_id)
        #Change title if necessary
        if (form2.title.data != chosenAssessment.title):
            #Must still be a unique name
            for a in assessments:
                if form2.title.data == a.title:

                    flash(f"An assessment with the name {a.title} already exists")
                    newName = False
        
            if newName == True:  
                chosenAssessment.title =  form2.title.data
                db.session.commit()
                changed = True
        
        #change course code if necessary 
        if (form2.code.data != chosenAssessment.module_code):
            chosenAssessment.module_code = form2.code.data
            db.session.commit()
            changed = True

        #change dealine date if necessary
        if (form2.dueDate.data != chosenAssessment.deadline_date):
            chosenAssessment.deadline_date = form2.dueDate.data
            db.session.commit()
            changed = True

        #change description if necessary
        if (form2.description.data != chosenAssessment.description):
            chosenAssessment.description = form2.description.data
            db.session.commit()
            changed = True
        
        #change completed if necessary
        if (form2.completed.data != chosenAssessment.completed):
            chosenAssessment.completed = form2.completed.data
            db.session.commit()
            changed = True

        #Only flash message if a change was made
        if changed == True:
            flash(f"Successfully changed {chosenAssessment.title}")

                


    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit, ChooseForm=form1, EditForm=form2, assessments=assessments, valid=valid, chosenAssessment=chosenAssessment)