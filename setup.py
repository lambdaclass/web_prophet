import os
from flask import Flask
from flask_bootstrap import Bootstrap

UPLOAD_FOLDER = './uploads'

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app(name):
    app = Flask(name)
    Bootstrap(app)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app
