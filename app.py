# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  props = {
    "categories" : "breakfast shouter",
    "board" : "chan"
  }
  return render_template("index.html", time=datetime.now(), props=props)

@app.route('/dog')
def dog_quiz():
  props = {
    "categories" : "breakfast shouter",
    "board" : "chan"
  }
  return render_template("dog.html", time=datetime.now(), props=props)
  
@app.route('/cat')
def cat_quiz():
  props = {
    "categories" : "breakfast shouter",
    "board" : "chan"
  }
  return render_template("cat.html", time=datetime.now(), props=props)