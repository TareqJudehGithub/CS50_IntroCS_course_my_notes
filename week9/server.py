from flask import Flask, render_template, request

# Instantiating an app object from Flask class
app = Flask(__name__)


# routes
@app.route("/")
def index():
    year = 2021
    return render_template(
      "index.html",    
      name=request.args.get("name", "world"), # the 2nd arg "world" is a default arg
      year=year
      )

# get Form
@app.route("/greet")
def greet():
  # Declare a name variable with user input value in web page url.
  name = request.args.get("name")
  return render_template(
    "greet.html",
    name=name
    )

# Username
@app.route("/username/<string:user>")
def username(user):
  return render_template("greet.html", user=user)


if __name__ == ("__main__"):
    app.run()