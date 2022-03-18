from hashlib import new
from flask import Blueprint, render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import models
import app

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
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
            new_user = models.User(username=username, email=email, password=generate_password_hash(
            password, method='sha256'))
            app.db.session.add(new_user)
            app.db.session.commit()
            session['user_id'] = new_user.id
            # return redirect(url_for('index'))

    return render_template('sign-up.html')

@auth.route('/login')
def login():
    return render_template('login.html')