from flask import Flask, render_template, request, session, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/socialnetwork'
app.secret_key='thisissecretkey'
db = SQLAlchemy(app)



class Userid(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.Integer(), nullable=False, unique=True)
    time = db.Column(db.String(12), nullable=False, unique=True)

    def __init__(self, email, password, time):
        self.email=email
        self.password=password
        self.time=time

@app.route("/")
def home():
    return render_template('index.html')




@app.route("/login", methods=['GET','POST'])
def login():
    if request.method=='POST':
        usernamel = request.form.get('username')
        passwordl = request.form.get('password')

        if usernamel!="" and passwordl!="":
            int_pass = int(passwordl)
            data_list = Userid.query.filter_by(email=usernamel)
            for elements in data_list:
                if int_pass==elements.password:
                    flash("Login Successful.")
                    return redirect("/")
                else:
                    flash("Wrong Password")
        else:
            flash("Invalid Entry!")
    return render_template('login.html')

@app.route("/create", methods=['GET','POST'])
def create():
    if request.method=='POST':
        usernamec = request.form.get('username')
        passwordc = request.form.get('password')
        time = datetime.now()
        if usernamec!="":
            creating = Userid(email=usernamec, password=passwordc, time=time)
            db.session.add(creating)
            db.session.commit()
            flash("Account Created Successfully.")
            return redirect("/create")
        else:
            flash("Invalid Entry!")
    return render_template('create.html')

app.run(debug=True)
