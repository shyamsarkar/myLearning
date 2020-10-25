from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/website4'
db = SQLAlchemy(app)


class Posts(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(25), nullable=False)


@app.route("/")
def home():
    posts = Posts.query.all()
    return render_template('index.html', posts=posts)


@app.route("/add", methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        adding = Posts(title=title, content=content, date=datetime.now())
        db.session.add(adding)
        db.session.commit()
    return render_template('add.html')


@app.route("/post/<string:serial>", methods=['GET'])
def post_route(serial):
    post = Posts.query.filter_by(serial=serial)
    return render_template('post.html', post=post)


app.run(debug=True)
