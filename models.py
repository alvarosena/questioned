from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True, nullable=False)
    biography = db.Column(db.String(200), nullable=True)
    url = db.Column(db.String(200), nullable=True) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship('Post')
    likes = db.relationship('Like')
    comments = db.relationship('Comment')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.String, db.ForeignKey('user.id'))
    likes = db.relationship('Like')
    comments = db.relationship('Comment')

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    user_id = db.Column(db.String, db.ForeignKey('user.id'))

