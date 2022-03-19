from functools import wraps
from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import models
import app

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        user = models.User.query.filter_by(email=email).first()

        if user:
            flash('User already exists', category='error')
        elif not username:
            flash('Username must is incorrect.')
        elif not email:
            flash('Email must is incorrect.')
        elif not password:
            flash('Password must is incorrect.')
        elif len(password) < 8:
            flash('Your password must have 8 chars minimum.', category='error')
        else:
            new_user = models.User(name=name, username=username, email=email, password=generate_password_hash(
            password, method='sha256'))
            app.db.session.add(new_user)
            app.db.session.commit()
            session['user_username'] = new_user.username
            return redirect(url_for('views.index'))

    return render_template('sign-up.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = models.User.query.filter_by(email=email).first()

        if user:
            password_match = check_password_hash(user.password, password)
            if not password_match:
                flash('Password is incorrect.')
            else:  
                session['user_username'] = user.username
                return redirect(url_for('views.index'))

    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_username") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function