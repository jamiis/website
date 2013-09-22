from flask import render_template, url_for, send_file
from app import app

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/partials/<name>')
def partial(name):
    return send_file('templates/partials/{0}'.format(name))
