from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/website11'

class Details(db.Model):
    serial=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(50))
    content=db.Column(db.String(100))



@app.route("/")
def home():
    elements = Details.query.all()
    return render_template('index.html', passed_data=elements)



@app.route("/page/<string:number>")
def page_number(number):
    number=int(number)
    elements = Details.query.paginate(per_page=5, page=number)
    return render_template('pages.html', passed_data=elements, number=number)



@app.route("/add", methods=['GET','POST'])
def adddata():
    if request.method=='POST':
        title = request.form.get('title')
        content = request.form.get('content')
        add_to_db = Details(title=title,content=content)
        db.session.add(add_to_db)
        db.session.commit()
        return redirect(url_for('adddata'))
    return render_template('add.html')


app.run(debug=True)