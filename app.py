from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    return "The flask Server is Running"

@app.route("/index")
def mbsa():
    return render_template('index.html')

