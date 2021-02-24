from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<path:path>")
def home(path = None):
    return "Hello World!"
