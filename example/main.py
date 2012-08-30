import sys

sys.path.insert(0, '../')

from flask import Flask, Blueprint
from flask import render_template

import flask_util_js

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<int:myid>')
def show_id():
    return 'ok'




bpt = Blueprint('sub', __name__)

@bpt.route('/<x>', defaults=dict(x=1))
def bpt_index(x):
    return 'ok'

app.register_blueprint(bpt, url_prefix='/sub')

    
flask_util_js.install(app)

if __name__ == '__main__':
    app.run(debug=True)
