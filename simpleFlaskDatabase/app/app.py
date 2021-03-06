#code partially taken from SQLAlchemy Quickstart page
#Source: http://flask-sqlalchemy.pocoo.org/2.3/quickstart/

from flask import render_template, request, redirect, url_for
from __init__ import initdb
from models import db, User

app = initdb()

@app.route('/')
def index():
    user = User.query.all()
    return render_template('index.html', user=user)

@app.route('/post_user', methods=['POST'])
def post_user():
    user = User(request.form['username'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_user', methods=['GET', 'POST', 'DELETE'])
def delete_user():
    user = User.query.filter_by(username = request.form['username']).first()

    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('index'))

if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=5000)
