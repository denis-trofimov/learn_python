#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""Hello World!"""


from flask import Flask
import get_weather


app = Flask(__name__)


@app.route("/")
def index():
    try:
        text_weather = get_weather.get_weather(
            get_weather.CITY_ID,
            get_weather.APP_ID
        )
        return text_weather
    except:
        return "Прогноз сейчас недоступен"


if __name__ == "__main__":
    app.run()
