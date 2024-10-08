from flask import render_template, flash
from app import app
from .forms import CalculatorForm

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