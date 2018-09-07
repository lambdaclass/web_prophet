import os
import pandas as pd
from validation import validate
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import Flask, request, Response, render_template, flash, redirect, url_for

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['csv'])
APP_DIR = os.path.dirname(os.path.realpath(__name__))

app = Flask(__name__)
Bootstrap(app)

def main(app):
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True)

if __name__ == '__main__':
    main(app)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def put_flash(validations):
    if validations == []:
        flash('File Uploaded', 'success')
    else:
        [flash(err, 'danger') for err in validations]
            

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
        
    elif request.method == 'POST':
        if 'upload' not in request.files:
            flash('No file uploaded', 'danger')
            return redirect(url_for('index'))
        file = request.files['upload']  
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            validations = validate(df)
            put_flash(validations)
            return redirect(url_for('index'))
        else:
            flash('Error: wrong extension', 'danger')
            return redirect(url_for('index'))
