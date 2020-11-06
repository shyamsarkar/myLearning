from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/website3'

class Login(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(20), nullable=False)


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        username = request.form.get('email1')
        pass_word = request.form.get('password1')
        login_db = Login(email=username, password=pass_word)
        db.session.add(login_db)
        db.session.commit()
        return redirect('/')
    return render_template("index.html")

app.run(debug=True)