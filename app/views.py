import os, datetime, psycopg2
from app import app, db, login_manager
from app.models import Post, Like, Follow, User
from flask import render_template, request, jsonify, send_file, redirect, url_for, flash, session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


########################## LOGIN MANAGEMENT #############################################################
########################## LOGIN MANAGEMENT #############################################################
########################## LOGIN MANAGEMENT #############################################################

@app.route('/api/v1/register', methods=['POST'])
def register():
    #Get POST form data and shove it up the database
    data = request.json

    user = User(
        username=data.get('username'),
        password=data.get('password'),
        firstname=data.get('firstname'),
        lastname=data.get('lastname'),
        email=data.get('email'),
        location=data.get('location'),
        biography=data.get('biography'),
        profile_photo=data.get('profile_photo'),
        joined_on=datetime.datetime.now()
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'})

@app.route('/api/v1/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Invalid username or password'})

@app.route('/api/v1/logout', methods=['POST'])
def logout():
    logout_user()
    flash("You are now logged out")
    return jsonify({'message': 'Successfully logged out.'})


########################## END LOGIN MANAGEMENT #############################################################
########################## END LOGIN MANAGEMENT #############################################################
########################## END LOGIN MANAGEMENT #############################################################




########################## APPLICATION FUNCTIONALITY #############################################################
########################## APPLICATION FUNCTIONALITY #############################################################
########################## APPLICATION FUNCTIONALITY #############################################################
@app.route('/api/v1/users/<int:user_id>/posts', methods=['POST'])
# @login_required()
def add_post(user_id):
    #Current_user is defined in the imports. Should just be the currently logged in user.
    if current_user != user_id:
        return jsonify({'message': 'Unauthorized access.'})
    data = request.get_json()
    caption = data.get('caption')
    photo = data.get('photo')
    created_on = data.get('created_on')

    post = Post(
        caption=caption, 
        photo=photo, 
        user_id=user_id, 
        created_on=created_on)
    
    db.session.add(post)
    db.session.commit()

    return jsonify({'message': 'Post created successfully.'})


@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
@login_required
def get_user_posts(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        return jsonify({'error': 'User not found'})
    
    if current_user != user:
        return jsonify({'error': 'Unauthorized access'})
    
    posts = Post.query.filter_by(user_id=user_id).all()
    return jsonify({'posts': [post.to_dict() for post in posts]})


@app.route('/api/v1/users/<int:user_id>/follow', methods=['POST'])
@login_required
def follow_user(user_id):
    # Check if the user being followed exists
    target_user = User.query.filter_by(id=user_id).first()
    if not target_user:
        return jsonify({'message': 'User does not exist'})

    # Create the follow relationship between current user and target user
    follow = Follow(current_user.id, user_id)
    db.session.add(follow)
    db.session.commit()

    return jsonify({'message': 'Successfully followed user'})


@app.route('/api/v1/posts', methods=['GET'])
@login_required
def get_all_posts():
    posts = Post.query.all()
    post_list = []
    for post in posts:
        post_list.append({
            'id': post.id,
            'caption': post.caption,
            'photo': post.photo,
            'user_id': post.user_id,
            'created_on': post.created_on.strftime('%Y-%m-%d %H:%M:%S') #DateTime YMD : HMS format. Can fix up in front end, probably.
        })
    return jsonify(post_list)


@app.route('/api/v1/posts/<int:post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Post.query.get(post_id)
    if not post:
        return jsonify({'message': 'Post not found'})

    user_id = current_user.id

    like = Like.query.filter_by(user_id=user_id, post_id=post_id).first()
    if like:
        return jsonify({'message': 'User already liked this post'})

    like = Like(user_id=user_id, post_id=post_id)
    db.session.add(like)
    db.session.commit()

    return jsonify({'message': 'Post liked successfully'})


########################## END APPLICATION FUNCTIONALITY #############################################################
########################## END APPLICATION FUNCTIONALITY #############################################################
########################## END APPLICATION FUNCTIONALITY #############################################################


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
# Basically, don't touch.
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()