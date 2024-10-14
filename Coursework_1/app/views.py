from flask import render_template
from app import app

@app.route('/', methods=['GET', 'POST'])
def home():
    home={'description':"Use this page to view all assessments, filter by completion and view assessment details"}
    return render_template('home.html', title='View Assessments', home=home)

@app.route('/addNew', methods=['GET', 'POST'])
def addNew():
    addNew={'description':"Use the form below to add a new assessment to the data base, every field must have a value"}
    return render_template('addNew.html', title='Add Assessments', addNew=addNew)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    edit={'description':"Amend assessment details or move assessments to completed using the form below"}
    return render_template('edit.html', title='Edit Assessments', edit=edit)