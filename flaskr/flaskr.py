#all import 
from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# config variable is only upper case
DATABASE = '/tmp/flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
#app.config.from_object(__name__)
app.config.from_envvar("FLASKR_SETTINGS", silent=True)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()
    
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_connect
def before_connect():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.after_connect
def after_connect():
    g.db.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337)
   
