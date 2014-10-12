#!/usr/bin/env python2.7

from flask import Flask
from flask.ext import login
import sqlite3

from config import *

app = Flask(__name__)
conn = sqlite3.connect(DATABASE_FILENAME)
cur = conn.cursor()

# login stuff
login_manager = login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(zid):
    #return db.session.query(User).get(zid)
    res = cur.execute('''
    SELECT zid, first_name, surname FROM users
    ''')

    if res:
        row = res.fetchone()
        obj = {
            'zid': row[0],
            'first_name': row[1],
            'surname': row[2]
        }
        return obj

@app.route("/")
def index():
    return 'wob'

if __name__ == "__main__":
    app.run(debug=True)