#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
#=============================================================================
#
#     FileName: flask_util_js.py
#         Desc: provide flask_util.js
#               在 app.config 中可以配置:
#                   FLASK_UTIL_JS_PATH: flask_util.js 的url路径
#                   FLASK_UTIL_JS_ENDPOINT: flask_util.js 的endpoint
#
#       Author: dantezhu
#        Email: zny2008@gmail.com
#     HomePage: http://www.vimer.cn
#
#      Created: 2012-07-09 17:23:51
#      Version: 0.1
#      History:
#               0.1   | dantezhu | 2012-08-30 22:54:33 | 正式版本
#               0.0.1 | dantezhu | 2012-07-09 17:23:51 | initialization
#
#=============================================================================
'''

from flask import Response
from flask import render_template_string

FLASK_UTIL_JS_PATH = '/flask_util.js'

FLASK_UTIL_JS_TPL_STRING = '''
var flask_util = function() {
    var url_map = {
        {% for k, v in url_map.items() %}
            {% if not loop.first %}
            ,
            {% endif %}

            '{{ k }}':{
                rule: '{{ v[0].rule }}',
                defaults: {{ v[0].defaults or {} }}
            }
        {% endfor %}
    };

    function url_encode(clearString) {
        var output = '';
        var x = 0;
        clearString = clearString.toString();
        var regex = /(^[a-zA-Z0-9-_.]*)/;
        while (x < clearString.length) {
            var match = regex.exec(clearString.substr(x));
            if (match != null && match.length > 1 && match[1] != '') {
                output += match[1];
                x += match[1].length;
            } else {
                if (clearString.substr(x, 1) == ' ') {
                    output += '+';
                }
                else {
                    var charCode = clearString.charCodeAt(x);
                    var hexVal = charCode.toString(16);
                    output += '%' + ( hexVal.length < 2 ? '0' : '' ) + hexVal.toUpperCase();
                }
                x++;
            }
        }
        return output;
    }

    function url_for(endpoint, params) {
        if (!params) {
            params = {};
        }
        if (!url_map[endpoint]) {
            return '';
        }
        var rule = url_map[endpoint]['rule'];
        var defaults = url_map[endpoint]['defaults'];

        for(var k in defaults) {
            if (!(k in params)) {
                params[k] = defaults[k];
            }
        }

        var used_params = {};


        var rex = /\<\s*(\w+:)*(\w+)\s*\>/ig;

        var path = rule.replace(rex, function(_i, _0, _1) {
            if (params[_1]) {
                used_params[_1] = params[_1];
                return url_encode(params[_1]);
            } else {
                return '';
            }
        });

        var query_string = '';

        for(var k in params) {
            if (used_params[k]) {
                continue;
            }

            var v = params[k];
            if(query_string.length > 0) {
                query_string += '&';
            }
            query_string += url_encode(k)+'='+url_encode(v);
        }

        var url = path;
        if (query_string.length > 0) {
            url += '?'+query_string;
        }

        return url;
    }

    return {
        url_for: url_for
    }
}();
'''

def install(app):
    """
    安装到app上
    """
    path = app.config.get('FLASK_UTIL_JS_PATH', FLASK_UTIL_JS_PATH)
    endpoint = app.config.get('FLASK_UTIL_JS_ENDPOINT', None)

    @app.route(path, endpoint=endpoint)
    def flask_util_js():
        url_map = app.url_map._rules_by_endpoint

        rv = render_template_string(
            FLASK_UTIL_JS_TPL_STRING, 
            url_map=url_map
            )

        return Response(rv, content_type='application/x-javascript')
