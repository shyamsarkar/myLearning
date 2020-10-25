from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "good"
app.permanent_session_lifetime = timedelta(minutes=10)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent = True
        task1 = request.form["nm"]
        if task1 !="":
            session["dict1"]=task1
            return redirect(url_for("user"))
        return render_template("login.html")
    else:
        if "dict1" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "dict1" in session:
        task2 = session["dict1"]
        return render_template("user.html", task3=task2)
    else:
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    if "dict1" in session:
        task_4 = session["dict1"]
        flash(f"{task_4}, You have been logged out successfully", "info" )
        session.pop("dict1", None)
        return redirect(url_for("login"))
    else:
        flash(f"Login to your account.")
        return redirect(url_for("login"))



if __name__=="__main__":
    app.run(debug=True)
