from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Posts(db.Model):
    serial=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80), nullable=False)
    slug=db.Column(db.String(25), nullable=False)
    content=db.Column(db.String(20), nullable=False)
    date=db.Column(db.String(12), nullable=True)



@app.route("/")
def home():
    return render_template('index.html', params=params)


@app.route("/post/<string:serial_num>", methods=['GET'])
def post_route(serial_num):
    post = Posts.query.filter_by(serial=serial_num)
    return render_template('postslug.html', post=post)


app.run(debug=True)