from flask import Flask, render_template
from datetime import datetime
import requests



app = Flask(__name__)


@app.route('/')
def hello_world():

  now = datetime.now()
  xmas = datetime(now.year, 12, 25) 
  delta = xmas - now
  final = delta.days
  message = "fuck christmas"
  if final > 0:
    message = "there are " + str(final) + " days until Christmas"
  elif final == 0:
    message = "It's Christmas!" 
  elif final < 0:
    message = "it's my birthday soon!"

  my_list = ['tikka t1X', 'tikka T3x', 'Lee Enfield', 'Mauser M96'] 

  r = requests.get("https://api.nasa.gov/planetary/apod", params={'api_key':'7GNTBFqluVt7sD4enKtgNt2ZL6chJmRYsymOqBvt'})

  nasa = r.json()

  print(nasa)

  return render_template("index.html", message=message, my_list=my_list, nasa=nasa)

# the web address is https://code-playground.onrender.com/

# to run the code click the fork icon on the far left, fill in the box with "What did you change?" and click "Commit & push", give it a few minutes (!) and look at the web page

# do not put any passwords in functions or variables, I'll show you how to do it