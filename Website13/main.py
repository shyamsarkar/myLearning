from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5432/cars_api"
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class CarsModel(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())

    def __init__(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors

    def __repr__(self):
        return f"<Car {self.name}>"


@app.route("/")
def home():
    name = "firstname"
    model = "firstmodel"
    doors = "firstdoor"
    entry_1 = CarsModel(name=name, model=model, doors=doors)
    db.session.add(entry_1)
    db.session.commit()
    return "successfull"

app.run(debug=True)