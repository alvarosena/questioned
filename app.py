from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import *
from auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

app.register_blueprint(auth, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)