from setuptools import setup
import flask_util_js

setup(
    name="flask_util_js",
    version=flask_util_js.__version__,
    zip_safe=False,
    platforms='any',
    py_modules=['flask_util_js'],
    install_requires=['flask'],
    url="https://github.com/dantezhu/flask_util_js",
    license="BSD",
    author="dantezhu",
    author_email="zny2008@gmail.com",
    description="flask's util in javascript. such as url_for etc.",
    )
