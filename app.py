from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def hello_world():
  now = datetime.now()
  xmas = datetime(now.year, 12, 25) 
  delta = xmas - now
  final = delta.days
  message = "fuck christmas"
  if final > 0:
    message = "there are " + final + " days until Christmas"
  elif final == 0:
    message = "It's Christmas!" 
  elif final < 0:
    message = "it's my birthday soon!"
  return render_template("index.html" message=message)

# the web address is https://code-playground.onrender.com/

# to run the code click the fork icon on the far left, fill in the box with "What did you change?" and click "Commit & push", give it a few minutes (!) and look at the web page

# do not put any passwords in functions or variables, I'll show you how to do it

# please sign up for render.com, let me know your user name and I'll add you to the team