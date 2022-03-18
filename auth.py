from flask import Blueprint, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash
import models
import app

auth = Blueprint('views', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # user = User.query.filter_by(email=email).first()

        # if user:
        #     pass
        
        new_user = models.User(username=username, email=email, password=generate_password_hash(
                password, method='sha256'))
        app.db.session.add(new_user)
        app.db.session.commit()
        return redirect('/sign-up')

    return render_template('sign-up.html')