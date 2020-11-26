from flask import Flask, render_template, request
import os
app = Flask(__name__)
# app.config['UPLOAD_FOLDER']='C:\\Users\\Sarkar\\PycharmProjects\\Websites\\Website10\\static'
@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        if request.files:
            image_file = request.files['value1']
            # image_file.save(os.path.join('app.config['UPLOAD_FOLDER']',image_file.filename))
            # image_file.save(os.path.join('static/upload_img', image_file.filename))
            # image_file.save(os.path.join('C:/Users/Sarkar/Music', image_file.filename))
            image_file.save(os.path.join('C:\\Users\\Sarkar\\Music', image_file.filename))
    return render_template('index.html')

app.run(debug=True)
