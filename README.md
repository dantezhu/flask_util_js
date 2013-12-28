flask_util_js
=============

flask's util in javascript. such as url_for etc.

### usage

###### install flask_util_js to your flask app

    from flask import Flask
    from flask_util_js import FlaskUtilJs

    app = Flask(__name__)

    fujs = FlaskUtilJs(app)

###### load flask_util.js in your html file

    {{ flask_util_js.js }}

###### use url_for in your js code

    var url = flask_util.url_for('a', {x:2, y:'/sdf'});
