from flask import Flask
from flask_login import LoginManager
import psycopg2
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate =   Migrate(app,db)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views

#Connect to database
conn = psycopg2.connect(
    host="localhost",
    database="project2",
    user="Project2Admin",
    password="Password123"
)

cur = conn.cursor()

#Users init

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        location VARCHAR(255) NOT NULL,
        biography VARCHAR(255) NOT NULL,
        profile_photo VARCHAR(255) NOT NULL,
        joined_on DATE NOT NULL
    );
""")

#Follow init

cur.execute("""
    CREATE TABLE IF NOT EXISTS follows (
        id SERIAL PRIMARY KEY,
        follower_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL
    );
""")

#Ice Spice (Like) init

cur.execute("""
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        post_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL
    );
""")   

#(Post) Malone init

cur.execute("""
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        caption VARCHAR(255) NOT NULL,
        photo VARCHAR(255) NOT NULL,
        user_id INTEGER NOT NULL,
        created_on DATE NOT NULL
    );
""") 

conn.commit()

cur.close()
conn.close()