from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/application", methods=["POST","GET"])
def application():
    if request.method == "POST":
        take1 = request.form["nm"]
        return redirect(url_for("user",variable1=take1))
    else:
        return render_template("login.html")

@app.route("/<variable1>")
def user(variable1):
    return f"<h1>Hello {variable1}.</h1>"

if __name__ =="__main__":
    app.run(debug=True)