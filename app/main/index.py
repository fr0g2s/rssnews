from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/main', methods=['GET'])
def index():
    return render_template('/main/index.html')

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('init_db.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.befre_connect()
def before_connect():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.after_connect
def after_connect(response):
    g.db.close()
