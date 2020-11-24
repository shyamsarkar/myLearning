from flask import Flask, render_template, request
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER']='C:\\Users\\Sarkar\\PycharmProjects\\Websites\\Website10\\static'
@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        if request.files:
            uploaded_image = request.files['value1']
            uploaded_image.save(os.path.join(app.config['UPLOAD_FOLDER'],uploaded_image.filename))
    return render_template('index.html')

app.run(debug=True)