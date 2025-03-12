from flask import Flask, render_template, request, redirect, url_for
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/many_relation'
db = SQLAlchemy(app)
app.secret_key = "this-is-secret-key"

class Person(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Address(db.Model):
    aid = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.pid'), nullable=False)


@app.route('/')
def home():
    return render_template('relation.html')

@app.route('/personname', methods=['GET','POST'])
def personname():
    if request.method=='POST':
        name = request.form.get('name')
        OBJ = Person(name=name)
        db.session.add(OBJ)
        db.session.commit()
    return "Successful..."

@app.route('/addressname', methods=['GET','POST'])
def addressname():
    if request.method=='POST':
        email = request.form.get('email')
        personname = request.form.get('personname')
        person_id = Person.query.filter_by(name=personname).first()  #this is working well
        Obj = Address(email=email, person=person_id)
        db.session.add(Obj)
        db.session.commit()
        return "Successful..."
    return "microsoft"


@app.route('/show')
def Show():
    allName =[]
    Obj = Person.query.all()
    ObjHome = Address.query.all()
    for element in Obj:
        allName.append(element.name)
    allName = json.dumps(allName)
    return allName

@app.route('/houses')
def Houses():
    allName = []
    Names = Person.query.all()
    for nameOnly in Names:
        for home in nameOnly.addresses:
            allName.append(home.email)
    # return redirect(url_for('home'))
    allName = json.dumps(allName)
    return allName


if __name__ == "__main__":
    app.run(debug=True)