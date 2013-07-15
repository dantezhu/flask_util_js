flask_util_js
=============

flask's util in javascript. such as url_for etc.

### usage

###### install flask_util_js to your server app

    from flask import Flask
    from flask_util_js import FlaskUtilJs

    app = Flask(__name__)

    fujs = FlaskUtilJs(app)

###### inject fujs to template context

    @app.context_processor
    def inject_fujs():
        return dict(fujs=fujs)

###### load flask_util.js in your html file

    {{ fujs.js }}

###### use url_for in your js file

    var url = flask_util.url_for('sub.bpt_index', {y:2, x:'/sdf'});
