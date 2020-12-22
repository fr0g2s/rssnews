from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
	return 'main page'

@app.route('/add-rss/<rss>')
def add_rss(rss):
	return 'add rss: %s' % rss

@app.route('/edit-rss/<rss>')
def edit_rss(rss):
	return 'edit rss: %s' % rss

@app.route('/remove-rss/<rss>')
def remove_rss(rss):
	return 'remove rss: %s' % rss


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0', port=8080)

