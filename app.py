import os
import pandas as pd
from validation import validate
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import request, Response, render_template, flash, redirect, url_for
from prophet_util import create_plots
from config import create_app, allowed_file

app = create_app(__name__)

if __name__ == '__main__': 
    app.run(debug=True)

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
            filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
            file.save(filepath)
            df = pd.read_csv(filepath)
            validations = validate(df)
            if validations == []:
                create_plots(filepath)
                return redirect(url_for('show'))
            else:
                put_flash(validations)
            return redirect(url_for('index'))
        else:
            flash('Error: wrong extension', 'danger')
            return redirect(url_for('index'))

@app.route('/show', methods=['GET'])
def show():
    return render_template('show.html')
