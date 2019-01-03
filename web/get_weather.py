#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""openweathermap_test.py API Access current weather data for any location on Earth including over 200,000 cities! Current weather is frequently updated based on global models and data from more than 40,000 weather stations. Data is available in JSON, XML, or HTML format."""


import requests
CITY_ID = 524901
APP_ID = "2da387b1f95b2443f187149f77e9f4a8"

def get_weather(city_id, appid):
    """ Get current weather.

        :returns: current weather``dict``
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"id": city_id, "appid": appid, "units": "metric"}
    responce = requests.get(url, params=params)
    if responce.status_code == 200:
        return f"Сейчас {responce.json()['main']['temp']} C"
    else:
        raise Exception(f"Error: {responce.status_code} {responce.reason}")


if __name__ == "__main__":
    text_weather = get_weather(CITY_ID, APP_ID)
    print(text_weather)
