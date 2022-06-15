# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from model import get_breakfast_rating
from datetime import datetime

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
# why do we need this when we can have multiple routes without flask? with just linking html pages
@app.route('/')
@app.route('/index')
def index():
  props = {
    "title" : "breakfast shouter",
    "name" : "chan"
  }
  return render_template("index.html", time=datetime.now(), props=props)

@app.route('/results', methods = ['GET', 'POST'])
def results():
    # why request? how does the method get this?
    if request.method == "POST":
      print(request.form['breakfast'])
      breakfast = request.form['breakfast']
      name = request.form['nickname']
      rating = get_breakfast_rating(breakfast)
      return render_template("results.html", breakfast = breakfast, name = name, rating = rating)
    else:
      # when running on replit, getting error but works in separate tab
      return redirect("/")
  
@app.route('/secret')
def secret():
    return "<h1>secret chan</h1>"
