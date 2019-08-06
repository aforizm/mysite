from flask import Flask, url_for
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		name = request.form['url']
		return render_template('hello.html', name=name)
	else:
		return render_template('hello.html')

@app.route('/', methods=['GET', 'POST'])
def getvideo():
	if request.method == 'POST':
		return 'post'
	else:
		return 'not post'


if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')