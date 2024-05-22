#!/usr/bin/python3
"""Flask web application that displays 'Hello HBNB!'"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

