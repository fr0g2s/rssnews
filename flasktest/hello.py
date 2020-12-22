from flask import Flask, url_for, render_template, Markup
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world'

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST':
		do_the_login()
	else:
		show_the_login_form()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=Markup(name).striptags())


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=8080)
