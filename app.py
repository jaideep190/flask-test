from flask import Flask, render_template
from flask import request
import requests
import time

app = Flask(__name__)



@app.route("/")
def start():
    while True:
        response = requests.get("https://smartbp-backend.onrender.com/")
        time.sleep(30)
    return "The flask Server is Running"


@app.route("/index")
def mbsa():
    while True:
        response = requests.get("https://smartbp-backend.onrender.com/")
        time.sleep(30)
    return render_template('index.html')

