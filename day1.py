from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Hello Er Body<h1>'
@app.route("/fave")
def favorite5():
    return '<h1>Bye Bye<h1>'