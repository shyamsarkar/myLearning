from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/onemany'
db = SQLAlchemy(app)
app.secret_key = "thisissecretkey"

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))


@app.route('/')
def home():
    return render_template('index.html')

<<<<<<< HEAD
=======
"""
>>>>>>> 2bef6ead9048f140f7a3a75094a1d3f679f8e060
@app.route('/human', methods=['GET','POST'])
def human():
    if request.method=='POST':
        name = request.form.get('name')
        entry_person = Person(name=name)
        db.session.add(entry_person)
        db.session.commit()
<<<<<<< HEAD
        return '<h1>Name Entered Successfully <a href="/">Home</a></h1>'
    return redirect(url_for('home'))
=======
        return '<h1>Name Entered Successfully</h1>'
    return redirect(url_for('home'))"""
>>>>>>> 2bef6ead9048f140f7a3a75094a1d3f679f8e060

@app.route('/animal', methods=['GET','POST'])
def animal():
    if request.method=='POST':
<<<<<<< HEAD
        hname = request.form.get('hname')
        animal = request.form.get('pname')
        owner = Person.query.filter_by(name=hname).first()
        entry_animal = Pet(name=animal, owner=owner)
        db.session.add(entry_animal)
        db.session.commit()
        return '<h1>Animal Name Added Successfully <a href="/">Home</a></h1>'
    return redirect(url_for('/'))
=======
        owner = request.form.get('pname')
        animal = request.form.get('animal')
        entry_person = Person(name=owner)
        entry_animal = Pet(name=animal, owner=entry_person)
        db.session.add(entry_person)
        db.session.add(entry_animal)
        db.session.commit()
        return '<h1>Animal Name Added Successfully <a href="/">Home</a></h1>'
    return render_template('index.html')
>>>>>>> 2bef6ead9048f140f7a3a75094a1d3f679f8e060


if __name__ =='__main__':
    app.run(debug=True)