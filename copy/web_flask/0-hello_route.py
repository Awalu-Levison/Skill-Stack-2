#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'

@app.route('/jospin/', strict_slashes=False)
def lioapp():
    """lioadd"""
    return 'Hello lio add!'
@app.route('/', strict_slashes=False)
def homepage():
    """lioadd"""
    return 'Hello lio on home page!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
