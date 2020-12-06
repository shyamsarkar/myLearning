from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/website16'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

class Information(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(255), nullable=False)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if (email!='' and password!=''):
            hashed_pass = sha256_crypt.encrypt(password)
            entry = Information(email=email, password=hashed_pass)
            db.session.add(entry)
            db.session.commit()
            return redirect(url_for('home'))
        return "Enter Email and Password"
    return redirect(url_for('home'))

@app.route('/all')
def all():
    details = Information.query.all()
    return render_template('all.html', details=details)

@app.route('/login', methods=['GET','POST'])
def login():
    login_value = False
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        details = Information.query.filter_by(email=email)
        for elements in details:
            if (sha256_crypt.verify(password, elements.password)):
                login_value = True
    if login_value:
        return f"Login Successful {email}"
    return render_template('login.html')

@app.route('/edit', methods=['GET','POST'])
def edit():
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        details = Information.query.filter_by(email=email)
        for elements in details:
            print(elements.email, elements.password)
        details.email = email
        details.password = password
        db.session.commit()
    return render_template('edit.html')

app.run(debug=True)