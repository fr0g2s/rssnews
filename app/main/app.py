from __future__ import with_statement
from contextlib import closing
from flask import Flask, request, render_template, flash, redirect, url_for, g
from flask import current_app as app

import sqlite3
import rssparser
import rssmanager


app = Flask(__name__)

@app.route('/')
def show_main():
    return render_template('/show-articles.html')

@app.route('/add', methods=['GET'])
def add_rss():
    add_rss = ''
    error_msg = ''
    if request.method == 'GET':
        add_rss = request.args.get('rss', '')
        if add_rss != '':
            try:
                rssmanager.RssManager().addRss(g.db, rss)
                flash('Add new RSS success')
            except Exception as e:
                error_msg = e
    return render_template('/add-rss.html', add_rss=add_rss, error=error_msg)

@app.route('/edit', methods=['GET'])
def edit_rss():
    old_rss = ''
    new_rss = ''
    error_msg = ''
    if request.method == 'GET':
        old_rss = request.args.get('old', '')
        new_rss = request.args.get('new', '')
        if old_rss != '' and new_rss != '':
            try:
                rssmanager.RssManager().editRss(g.db, old_rss, new_rss)
            except Exception as e:
                error_msg = e
    return render_template('/edit-rss.html', old_rss=old_rss, new_rss=new_rss, error=error_msg)

@app.route('/del', methods=['GET'])
def del_rss():
    del_rss = ''
    error_msg = ''
    if request.method == 'GET':
        del_rss = request.args.get('rss','')
        if del_rss != '':
            try:
                rssmanager.RssManager().delRss(g.db, del_rss)
            except Exception as e:
                error_msg = e
    return render_template('/del-rss.html', del_rss=del_rss, error=error_msg)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('init_db.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        db.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.after_request
def after_request(response):
    return response

if __name__ == "__main__":
    app.debug = True
    app.config.from_object("config")
    g.rssmanager = rssmanager.RssManager()
    g.rssparser = rssparser.RssParser()
    
    init_db()

    app.run(host="0.0.0.0", port=1337)
