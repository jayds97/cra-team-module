from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def homepage():
    return render_template('home.html')

@app.route('/reg')
def register():
    return render_template('reg.html')

@app.route('/login')
def login():
    return render_template('login.html')
