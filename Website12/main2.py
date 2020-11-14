from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/shyamdb'
db =SQLAlchemy(app)

class User(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

@app.route("/")
def home():
    return 'Hello World'
