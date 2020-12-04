from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

# the web address is https://code-playground.onrender.com/

# to run the code click the fork icon on the far left, fill in the box with "What did you change?" and click "Commit & push", give it a few minutes (!) and look at the web page

# do not put any passwords in functions or variables, I'll show you how to do it

# please sign up for render.com, let me know your user name and I'll add you to the team