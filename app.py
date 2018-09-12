import os
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import request, Response, render_template, flash, redirect, url_for
from prophet_util import create_plots
import config
import validations as val

app = config.create_app(__name__)

if __name__ == '__main__': 
    app.run(debug=True)

def put_flash(validations):
    if validations == []:
        flash('File Uploaded', 'success')
    else:
        [flash(err, 'danger') for err in validations]
            
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
 
@app.route('/', methods=['POST'])
def upload():
    if 'upload' not in request.files:
        flash('No file uploaded', 'danger')
        return redirect(url_for('index'))
    file = request.files['upload']  
    if file and config.allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
        file.save(filepath)

        validations = val.validate_csv(filepath)
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
