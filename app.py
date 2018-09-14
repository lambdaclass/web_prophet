import os
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename
from flask import request, render_template, flash, redirect, url_for
import prophet_util
import config
import validations as val

app = config.create_app(__name__)


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
        filepath = get_filepath(file)
        file.save(filepath)
        validations = val.validate_csv(filepath)
        if not validations:
            prophet_util.create_plots(filepath)
            return redirect(url_for('show'))
        else:
            put_validation_flash(validations)
            return redirect(url_for('index'))

    else:
        flash('Error: wrong extension', 'danger')
        return redirect(url_for('index'))


@app.route('/show', methods=['GET'])
def show():
    return render_template('show.html')


def put_validation_flash(validations):
    if not validations:
        flash('File Uploaded', 'success')
    else:
        [flash(err, 'danger') for err in validations]

def get_filepath(file):
    filename = secure_filename(file.filename)
    return os.path.join(app.config['UPLOAD_DIR'], filename)


if __name__ == '__main__':
    app.run(debug=True)
