from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/website2"
class Posts(db.Model):
    serial=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(80), nullable=False)
    slug=db.Column(db.String(25), nullable=False)
    content=db.Column(db.String(200), nullable=False)
    date=db.Column(db.String(12), nullable=False)


@app.route("/")
def home():
    post = Posts.query.all()
    return render_template('index.html', post=post)



@app.route("/post/<string:serial>", methods=['GET','POST'])
def post_route(serial):
    post = Posts.query.filter_by(serial=serial).first()
    if request.method=='POST':
        title = request.form.get('title')
        slug = request.form.get('slug')
        content = request.form.get('content')
        date = datetime.now()
        if serial!='0':
            post.title = title
            post.slug = slug
            post.content = content
            post.date = date
            db.session.commit()
            return redirect('/post/'+serial)
        else:
            add_new_post = Posts(title=title, slug=slug, content=content, date=date)
            db.session.add(add_new_post)
            db.session.commit()

    return render_template('post.html', post=post, serial=serial)

app.run(debug=True)
