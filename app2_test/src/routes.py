from flask import Flask, request, render_template
from src.logic import my_function

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    n1 = request.form['number1']
    n2 = request.form['number2']
    n3 = request.form['number3']
    return my_function(n1, n2, n3)
