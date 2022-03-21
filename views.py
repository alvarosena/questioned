from flask import Blueprint, jsonify, redirect, render_template, request, flash, session, url_for
from auth import login_required
import models as models
import app

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        text = request.form.get('text')

        if len(text) < 1:
            flash('Write some text.', category='error')

        else:
            post = models.Post(text=text, user_username=session['user_username'])
            app.db.session.add(post)
            app.db.session.commit()
            return redirect(url_for('views.index'))

    posts = models.Post.query.all()
    return render_template('index.html', posts=posts)

@views.route('/like/<int:post_id>')
def like(post_id):
    post = models.Post.query.filter_by(id=post_id).first()
    like = models.Like(post_id=post_id, user=session['user_username'])

    app.db.session.add(like)
    app.db.session.commit()

    return jsonify({ 'likes': len(post['likes']) })

@views.route('/<string:username>')
def profile(username):
    user = models.User.query.filter_by(username=username).first()

    if user == None:
        flash(f"The account {username} doesn't exists, 404", category='error')
        return redirect(url_for('views.index'))

    posts = models.Post.query.filter_by(user_username=username).all()
    return render_template('profile.html', user=user, posts=posts)

