#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """displays c <text>"""
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is(text):
    """displays 'python is cool' by default"""
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_is(n):
    """displays n is a number"""
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)