from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///relationships.db'
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


@app.route('/', methods=['GET','POST'])
def home():
    if request.method=='POST':
        name = request.form.get('name')
        entry = Person(name=name)
        db.session.add(entry)
        db.session.commit()
        return '<h1>Successfull <a href="/">Home</a></h1>'
    return render_template('index.html')

@app.route('/all')
def pet():
    posts = Person.query.all()
    pets1 = Pet.query.all()
    for post in posts:
        print(post.id, post.name, post.pets)
    for animal in pets1:
        print(animal.id, animal.name, animal.owner_id)
    return redirect(url_for('home'))

@app.route('/pets', methods=['GET','POST'])
def persons():
    if request.method=='POST':
        name = request.form.get('name')
        owner = request.form.get('owner')
        entry1 = Pet(name=name, owner=owner)
        db.session.add(entry1)
        db.session.commit()
        return "<h1>Successfull</h1>"
    return render_template('index.html')


if __name__ =='__main__':
    app.run(debug=True)