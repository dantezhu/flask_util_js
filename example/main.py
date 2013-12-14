# -*- coding: utf-8 -*-

import sys

sys.path.insert(0, '../')

from flask import Flask, Blueprint
from flask import render_template, url_for

from flask_util_js import FlaskUtilJs

app = Flask(__name__)
app.config.from_object(__name__)

fujs = FlaskUtilJs(app)

@app.route('/')
def a():
    print url_for('b', name='dante', gender='male')
    return render_template('index.html')

@app.route('/b/', defaults=dict(name='shit'))
@app.route('/b/<name>')
def b(name):
    return name

if __name__ == '__main__':
    app.run(debug=True)
