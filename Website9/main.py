from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        taken_rupees = request.form.get('indian_rupees')
        return_rupees = int(taken_rupees)/75
        return render_template("index.html", usd_rupees=return_rupees,textline="This String is Taken From Flask Python")
    return render_template("index.html", textline="This String is Taken From Flask Python")

@app.route("/<variable1>")
def redirct(variable1):
    return f"hello {variable1}."

@app.route("/redt")
def redtd():
    return redirect(url_for("home"))

@app.route("/admin")
def admin():
    return redirect(url_for("redirct", variable1 = ", you are redirected to variable page"))


if __name__ == "__main__":
    app.run(debug=True)