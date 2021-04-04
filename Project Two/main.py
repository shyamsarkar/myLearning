from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/project2'
db = SQLAlchemy(app)
app.secret_key = 'this_is_project_two'
app.secret_key = 'this_website_is_for_complete_chatting'

class Createac(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    mobile = db.Column(db.Integer)
    email = db.Column(db.String(50))
    password = db.Column(db.String(30))
    date = db.Column(db.String(12))



@app.route('/')
def home():
    if ("email_id" in session) and ("pass_word" in session):
        query_email = Createac.query.filter_by(email=session['email_id'])
        for element in query_email:
            if element:
                if element.password==session['pass_word']:
                    print(f"1. home successful. user = {session['email_id']}")
                    return render_template('dashboard.html', user_fname=element.fname, user_lname=element.lname)
                else:
                    print("2. redirected to logout")
                    return redirect(url_for('logout'))
    return redirect(url_for('account'))

@app.route('/account', methods=['GET','POST'])
def account():
    if ("email_id" in session) and ("pass_word" in session):
        return redirect('/')
    if request.method=='POST':
        firstname = request.form.get('fname')
        lastname = request.form.get('lname')
        mobile_num = request.form.get('mobile')
        email_id = request.form.get('email')
        password = request.form.get('password')
        date = datetime.now()
        entry_detail = Createac(fname=firstname, lname=lastname,mobile=mobile_num,email=email_id,password=password,date=date)
        db.session.add(entry_detail)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('account.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if ("email_id" in session) and ("pass_word" in session):
        return redirect('/')
    if request.method=='POST':
        email = request.form.get('email')
        password = request.form.get('password')
        query_email = Createac.query.filter_by(email=email)
        # query_email = Createac.query.filter_by(email=email, password=password)

        for element in query_email:
            if element:
                if element.password==password:
                    print("3. login Success")
                    session['email_id'] = email
                    session['pass_word'] = password
                    return redirect(url_for('home'))
                else:
                    print("4. login failed!")
                    return f"<h1>Login Failed!. Please insert correct Password.<a href='/logout'>Return</a></h1>"
        return "Account not Found.<a href='/logout'>return</a>"
    return redirect(url_for('account'))

@app.route('/logout')
def logout():
    session.pop('email_id', None)
    session.pop('pass_word', None)
    return redirect(url_for('account'))


app.run(debug=True)