from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
from datetime import datetime


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)
app.secret_key = "thisissecretkey"

class Contacts(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)


class Posts(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(12), nullable=True)



@app.route("/")
def home():
    return render_template('index.html', params = params)

@app.route("/post", methods=['GET'] )
def post_route():
    post = Posts.query.all()
    return render_template('post.html', post=post)

@app.route("/post/<string:postslug>", methods=['GET'])
def post_slug(postslug):
    poststring = Posts.query.filter_by(slug=postslug)
    return render_template('postslug.html', poststring=poststring)


@app.route("/addpost", methods = ['GET', 'POST'])
def addpost():
    if (request.method == 'POST'):
        title = request.form.get('title')
        slug = request.form.get('slug')
        content = request.form.get('content')
        add_instance = Posts(title=title, slug=slug, content=content, date=datetime.now())
        db.session.add(add_instance)
        db.session.commit()
    return render_template('addpost.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/services")
def services():
    return render_template('services.html')




@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if(request.method=='POST'):
        name = request.form.get('name')
        phone = request.form.get('phone')
        email = request.form.get('email')
        message = request.form.get('message')
        entry = Contacts(name=name, mobile=phone, msg=message,email=email, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        flash("You message sent successful!", "information")
        return redirect(url_for("contact"))
    return render_template('contact.html')




@app.route("/portfolio-2-col.html")
def pf2():
    return render_template('portfolio-2-col.html')


@app.route("/portfolio-3-col.html")
def pf3():
    return render_template('portfolio-3-col.html')


@app.route("/portfolio-4-col.html")
def pf4():
    return render_template('portfolio-4-col.html')

@app.route("/portfolio-item.html")
def pf():
    return render_template('portfolio-item.html')

@app.route("/blog1")
def blog1():
    return render_template('blog-home-1.html')

@app.route("/blog2")
def blog2():
    return render_template('blog-home-2.html')

@app.route("/blog")
def blog():
    return render_template('blog-post.html')

@app.route("/full-width.html")
def full_width():
    return render_template('full-width.html')

@app.route("/sidebar.html")
def sidebar():
    return render_template('sidebar.html')

@app.route("/faq.html")
def faq():
    return render_template('faq.html')

@app.route("/404.html")
def error_msg():
    return render_template('404.html')

@app.route("/pricing.html")
def pricing():
    return render_template('pricing.html')
app.run(debug=True)
