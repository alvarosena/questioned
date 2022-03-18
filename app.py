from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return '<h1>Hello, Flask</h1>'

if __name__ == "__main__":
    app.run(debug=True)