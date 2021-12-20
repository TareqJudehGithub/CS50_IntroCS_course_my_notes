from flask import Flask, render_template, request, redirect
from markupsafe import escape


app = Flask(__name__)

REGISTRANTS = dict()

# CONSTANTS 
SPORTS = ["Dodgeball", "Soccer", "Basketball", "Volleyball"]



@app.route("/registrants")
def registrants():
   return render_template(
        escape("success.html"),
        registrants=REGISTRANTS
        )

@app.route("/register", methods=["GET", "POST"])
def index():
  if request.method == "GET":
    return render_template(
      escape("index3.html"),
      sports=SPORTS
      )
  
  if request.method == "POST":
    name = request.form.get("name")
    sport = request.form.get("sport")
    print(sport)
    
    # check for fields validations
    if  not name:
      return render_template(
        escape("error.html"), 
        message="Name Should not be empty."
      )
    elif not sport:
      return render_template(
        escape("error.html"), 
        message="Sport Should not be empty."
      )
    elif sport not in SPORTS:
      return render_template(
        escape("error.html"), 
        message="Invalid sport selected."
      )
    else:  
      REGISTRANTS[name] = sport
      return redirect("/registrants")