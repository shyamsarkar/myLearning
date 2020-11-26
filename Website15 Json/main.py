from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import json
app = Flask(__name__)
db = SQLAlchemy(app)
with open('config.json') as f:
    parameter = json.load(f)['parameter']
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/phpdb3'

class City(db.Model):
    serial = db.Column(db.Integer, primary_key=True)
    village = db.Column(db.String(50))


@app.route("/")
def home():
    return render_template('index.html', parameter=parameter)

@app.route("/take", methods=['GET','POST'])
def take():
    if request.method=='POST':
        # radiobtn = request.form.get('radiobutton')
        # print(radiobtn)

        # serial = request.form.get('serial')
        village = request.form.get('village')
        entry = City(village=village)
        db.session.add(entry)
        db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))


app.run(debug=True)