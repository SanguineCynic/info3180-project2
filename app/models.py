from . import db
from flask import Flask, request
from werkzeug.security import generate_password_hash

app = Flask(__name__)

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    user_id = db.Column(db.Integer)
    created_on = db.Column(db.DATE)

    def __init__(self, caption, photo, user_id, created_on):
        self.caption = caption
        self.photo = photo
        self.user_id = user_id
        self.created_on  = created_on

class Like(db.Model):

    __tablename__= "likes"

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

class Follow(db.Model):

    __tablename__ = "follows"

    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    location = db.Column(db.String(255))
    biography = db.Column(db.String(255))
    profile_photo = db.Column(db.String(255))
    joined_on = db.Column(db.DATE)

    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo, joined_on):
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = joined_on

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)