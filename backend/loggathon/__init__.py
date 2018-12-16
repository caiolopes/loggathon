import os
from flask import Flask
from flask_cors import CORS
#  from flask_sqlalchemy import SQLAlchemy
from tinydb import TinyDB, Query
from flask_qrcode import QRcode

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

CORS(app)
QRcode(app)
#  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#  db = SQLAlchemy(app)

db = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.json'))

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'media')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from loggathon import routes
