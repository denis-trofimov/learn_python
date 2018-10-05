#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Hello World!"""


from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
