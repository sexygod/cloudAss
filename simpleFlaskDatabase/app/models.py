#code partially taken from SQLAlchemy Quickstart page
#Source: http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return ('<User %r> <Email %r>' % (self.username, self.email))
