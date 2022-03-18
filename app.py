from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from models import *
from auth import auth
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db = SQLAlchemy(app)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)