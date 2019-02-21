#code partially taken from SQLAlchemy Quickstart page
#Source: http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

from flask import Flask
from models import db

def initdb():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:docker@postgres-docker:5432/postgres'

    app.app_context().push()
    db.init_app(app)
    db.create_all()
    return app
