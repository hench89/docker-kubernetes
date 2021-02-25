import redis
import time
from flask import Flask, request, render_template
from flaskapp import app
from flaskapp import cache
from logic.functions import my_function

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

def calculate_result():
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

@app.route('/')
def my_form():
    page_count = get_hit_count()
    return render_template('my_form.html', page_count=page_count)

@app.route('/', methods=['POST'])
def my_form_post():
    result_value = calculate_result()
    return render_template('my_result.html', result_value=result_value)
