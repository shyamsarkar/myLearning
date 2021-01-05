from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///two.db'

class Contacs(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))



# @app.route("/", methods = ['GET','POST'])
# def home():
#     if request.method=='POST':
#         firstname = request.form['nameone']
#         secondname = request.form['nametwo']
#         post = User(fname = firstname, lname = secondname)
#         db.session.add(post)
#         db.session.commit()
#     return render_template('index.html')

posts = Contacs.query.all()

for post in posts:
    print(post.name)



if __name__ == '__main__':
    app.run(debug=True)