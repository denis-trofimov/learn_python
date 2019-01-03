#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Hello World!"""


from flask import Flask
import get_weather


app = Flask(__name__)


@app.route("/")
def index():
    return get_weather.get_weather(get_weather.CITY_ID, get_weather.APP_ID)


if __name__ == "__main__":
    app.run()
