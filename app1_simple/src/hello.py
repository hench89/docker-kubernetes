from flask import Flask
from flask import request
from flask import Response

app = Flask(__name__)

@app.route("/")
@app.route("/<path:path>")
def home(path = None):
    return "Hello World!"