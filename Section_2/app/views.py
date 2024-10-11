from flask import render_template, flash
from app import app, db, models
import datetime
from .forms import CalculatorForm, PropertyForm

@app.route('/fruit')
def displayFruit():
    fruits = ["Apple", "Banana", "Orange", "Kiwi"]
    return render_template("fruit_with_inheritance.html",fruits=fruits)

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    form = CalculatorForm()
    if form.validate_on_submit():
        flash('Succesfully recieved form data. %s + %s =%s'%(form.number1.data, form.number2.data, form.number1.data + form.number2.data ))
    return render_template('calculator.html',
                           title='Calculator',
                           form=form)

@app.route('/new', methods=['GET', 'POST'])
def new():
    form = PropertyForm()
    if form.validate_on_submit():
        flash('Successfully entered property details')
        p = models.Property(address=form.address.data,start_date=datetime.datetime.utcnow(),duration=form.duration.data, rent=form.rent.data)
        db.session.add(p)
        db.session.commit()
    return render_template('new.html',
                            title='New Property',
                            form=form)
@app.route('/details', methods=['GET', 'POST'])
def details():
    properties = []
    for p in models.Property.query.all():
        properties.append(p)
    return render_template('details.html',
                            title='Properties',
                            properties=properties)

