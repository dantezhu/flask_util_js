flask_util_js
=============

flask's util in javascript. such as url_for etc.

### usage

###### install flask_util_js to your server app


    from flask import Flask
    import flask_util_js

    app = Flask(__name__)

    flask_util_js.install(app)


###### load flask_util.js in your html file

    <script src="{{ url_for('flask_util_js') }}" type="text/javascript" charset="utf-8"></script>

###### use url_for in your js file

    var url = flask_util.url_for('sub.bpt_index', {y:2, x:'/sdf'});
