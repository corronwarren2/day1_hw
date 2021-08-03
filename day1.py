from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = 'Top 5 Disney Rides'
    return render_template('index.html', title=title)

@app.route("/fave")
def favorite5():
    rides = ["Rise of the Resistance", " Tower of Terror", " Space Mountain", "Rock N Roller Coaster", "Avatar: Flight of Passage"]
    return render_template('fave.html', rides=rides)