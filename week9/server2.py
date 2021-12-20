from flask import Flask, render_template, request


# Instantiate a new object from Flask class
app = Flask(__name__)


# routes

# homepage
@app.route("/", methods=["GET", "POST"])
def index():
  
  # Using the same route for serving both get and post requests.
  # render the form html
  if request.method == "GET":
    return render_template("index2.html")
  
  # render the greet user page after submitting the form
  if request.method == "POST":
    username = request.form.get("name", "john smith".title())
    return render_template("greet2.html", username=username)


if __name__ == "__main__":
  app.run(debug=True)
  