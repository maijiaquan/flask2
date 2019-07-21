

import os

from flask import Flask
from flask import request
from flask import current_app
from werkzeug.utils import secure_filename
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/uploadImage')
def upload():
    return 'Upload Image'


@app.route('/downloadText')
def download():
    f = open('data.txt')
    a = f.read()
    f.close()
    return a

@app.route('/uploadText', methods=['GET', 'POST'])
def upload_text():
    if request.method == 'POST':
        print len(request.files)
        print request.get_data()
        return 'upload ok'
    else:
        return 'OK'

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part')
            return 'no file part, upload fail'
        else:    
            print('get the file')
            f = request.files['file']
            f.save('a.jpg')
            os.system("echo \"Hello World\"")
            os.system("python ../ano/FloorplanTransformation/pytorch/train.py --task=test_batch")

            return 'upload ok'
    else:
        return '''
    <!doctype html>
    <title>Upload new Picture</title>
    <h1>Upload new Picture</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

