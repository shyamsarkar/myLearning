from flask import Flask, render_template, request
from flask_mail import *

app = Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME'] = 'YourEmailID@gmail.com'
app.config['MAIL_PASSWORD'] = 'YourPassword'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sendmail", methods=['POST'])
def sendmail():
    title = request.form.get('title')
    content = request.form.get('content')
    msg = Message(subject=title,body = content, sender=app.config['MAIL_USERNAME'], recipients=['example@gmail.com'])

    mail.send(msg)
    return "Message Sent Successfully!<a href='/'>Home</a>"




if __name__ == '__main__':
    app.run(debug = True)
