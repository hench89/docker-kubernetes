from flask import Flask, request, render_template
from flaskapp import app
from logic.functions import my_function

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():

    try:
        
        n1 = int(request.form['number1'])
        n2 = int(request.form['number2'])
        n3 = int(request.form['number3'])
        status_code, my_value = my_function(n1, n2, n3)
        
        if (status_code == 0):
            return "error in inputs"
        return str(my_value)
    except:
        return "error"
