import os
from flask import Flask
from flask_bootstrap import Bootstrap

UPLOAD_DIR = './uploads'
IMG_DIR = './static/img'

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_upload_dirs():
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)     
    if not os.path.exists(IMG_DIR):
        os.makedirs(IMG_DIR)

def create_app(name):
    app = Flask(name)
    Bootstrap(app)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
    app.config['UPLOAD_DIR'] = UPLOAD_DIR
    create_upload_dirs()
    return app