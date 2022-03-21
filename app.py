from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from models import db
from auth import auth
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///questions.db'
db.init_app(app)
migrate = Migrate(app, db)

app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.register_blueprint(views, url_prefix='/')
app.register_blueprint(auth, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)