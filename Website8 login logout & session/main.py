from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta
app = Flask(__name__)

app.secret_key="my_secret"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/logout")
def logout():
    session.pop("dict_name", None)
    session.pop("dict_pass", None)
    return redirect(url_for('home'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    if ("dict_name" in session):
        return redirect(url_for("dashboard"))
    if request.method == 'POST':
        id_name = request.form.get('name')
        id_pass = request.form.get('password')
        session.permanent=True
        session["dict_name"] = id_name
        session["dict_pass"] = id_pass
        return redirect(url_for('dashboard'))
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if ("dict_name" in session):
        user = session["dict_name"]
        password = session["dict_pass"]
        return render_template("dashboard.html", user = user, password=password)
    return redirect(url_for("login"))

@app.route("/")
def home():
    if ("dict_name" in session):
        main_user = session["dict_name"]
        return render_template('index.html', user=main_user)
    else:
        return render_template('index.html')

app.run(debug=True)