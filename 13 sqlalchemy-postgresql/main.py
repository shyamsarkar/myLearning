from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/website15"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
#db.init_app(app)



class Colony(db.Model):
    #__tablename__ = 'cars'

    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    surname = db.Column(db.String(30))

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        

    def __repr__(self):
        return f"<Car {self.name}>"


@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        entry_1 = Colony(name=name, surname=surname)
        db.session.add(entry_1)
        db.session.commit()
    return render_template('index.html')

@app.route("/edit/<string:serial>", methods=['GET','POST'])
def post_route(serial):
    post = Colony.query.filter_by(serial=serial).first()
    if request.method=='POST':
        name = request.form.get('name')
        surname = request.form.get('surname')

        post.name = name
        post.surname = surname
        db.session.commit()
    return render_template("edit.html", serial=serial, name = post.name, surname = post.surname)

@app.route("/read")
def read():
    posts = Colony.query.all()
    return render_template("read.html", posts=posts)


@app.route("/delete/<string:serial>")
def delete(serial):
    posts = Colony.query.filter_by(serial=serial).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect("/")



app.run(debug=True)