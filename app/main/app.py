from __future__ import with_statement
from contextlib import closing
from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as app

import sqlite3
import rssparser
import rssmanager


app = Flask(__name__)

@app.route('/')
def show_main():
    return render_template('/show_articles.html')

@app.route('/add', method=['GET'])
def add_rss(rss):
    
    pass

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('init_db.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.befre_request()
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

if __name__ == "__main__":
    app.debug = True
    app.config.from_object("config")
    g.rssmanager = rssmanager.RssManager()
    g.rssparser = rssparser.RssParser()
    
    init_db()

    app.run(host="0.0.0.0", port=1337)
