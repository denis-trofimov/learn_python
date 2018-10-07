#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""openweathermap_test.py API Access current weather data for any location on Earth including over 200,000 cities! Current weather is frequently updated based on global models and data from more than 40,000 weather stations. Data is available in JSON, XML, or HTML format."""


import requests

def get_current(url):
#    req = requests.Request("GET", url, params=params)
    responce = requests.get(url)
    if responce.status_code == 200:
        return responce.json()
    else:
        raise Exception(f"Error: {responce.status_code} {responce.reason}")


if __name__ == "__main__":
    data_json = get_current("https://api.openweathermap.org/data/2.5/weather?id=524901&appid=12da387b1f95b2443f187149f77e9f4a8")
    print(data_json)
