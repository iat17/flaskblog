from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:'
db = SQLAlchemy(app)

@app.route('/', methods=['GET',])
def index():
    if request.method == 'GET':
        return 'Hello'