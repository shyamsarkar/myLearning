from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "good"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        task1 = request.form["nm"]
        session["dict1"]=task1
        return redirect(url_for("user"))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    if "dict1" in session:
        task2 = session["dict1"]
        return f"<h1>This is {task2}. You are logged in successfully.</h1>"
    else:
        return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
