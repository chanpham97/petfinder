# -- Import section --
from flask import Flask
from flask import render_template
from flask import request, redirect
from datetime import datetime
import sys
from model import get_breeds 

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html", time=datetime.now())

@app.route('/dog')
def dog_quiz():
  return render_template("dog.html", time=datetime.now())
  
@app.route('/cat')
def cat_quiz():
  return render_template("cat.html", time=datetime.now())

@app.route('/dog_results', methods = ['GET', 'POST'])
def dog_results():
    # why request? how does the method get this?
    if request.method == "POST":
      # print(request.form, file=sys.stdout)
      print(request.form, file=sys.stdout)
      experience = int(request.form['experience'])
      bark = int(request.form['bark'])
      shed = int(request.form['shed'])
      breeds = get_breeds(experience, bark, shed)
      props = {
        "experience": experience,
        "bark" : bark,
        "shed" : shed,
        "breeds" : breeds,
      }
      return render_template("dog_results.html", props = props)
    else:
      # when running on replit, getting error but works in separate tab
      return redirect("/")