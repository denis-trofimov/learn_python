#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""
    Как работает интернет
    URL - универсальный способ обращения к интернет-ресурсам
    Создаем простое веб-приложение
    Просматриваем и анализируем ответ удаленного сервера
    Библиотека requests
    Делаем сайт с прогнозом погоды на Flask и requests
    Передача параметров через URL
    Передача параметров методом GET
"""
from datetime import datetime
from flask import Flask, abort, request
from get_weather import get_current

city_id = 524901
appid = "2da387b1f95b2443f187149f77e9f4a8"
news_list = [
    {
        "id": 1,
        "title": "fastai v1 for PyTorch: Fast and accurate neural nets using modern best practices",
        "text": "fastai v1 for PyTorch: Fast and accurate neural nets using modern best practices",
        "date": "02 Oct 2018"
    },
    {
        "id": 2,
        "title": "Now anyone can train Imagenet in 18 minutes",
        "text": "Now anyone can train Imagenet in 18 minutes",
        "date": "10 Aug 2018"
    },
    {
        "id": 1,
        "title": "Google's AutoML: Cutting Through the Hype",
        "text": "Google's AutoML: Cutting Through the Hype",
        "date": "23 Jul 2018"
    },
]


app = Flask(__name__)


@app.route("/")
def index():
    data_weather = get_current(city_id, appid)
    cur_date = datetime.now().strftime("%d.%m.%Y")
    result = f"""<p>Дата: <b>{cur_date}</b></p>
    Город: <b>{data_weather['name']}</b><BR>
    Температура: <b>{data_weather['main']['temp']} C</b><BR>
    """
    return result


@app.route("/news")
def news_by_params():
    for item in request.args:
        print(item)
        print(request.args.get(item))
    try:
        limit = int(request.args.get('limit', 'all'))
    except:
        limit = 1
    colors = ['red', 'green', 'blue']
    color = request.args.get('color')
    if color not in colors:
       color = 'black'
    return f'<h1 style=\"color: {color}\">News: {limit}</h1>'


@app.route("/news/<int:news_id>")
def show_news(news_id):
    news_to_show = [news for news in news_list if news['id'] == news_id]
    if news_to_show:
        output = "<h1>%(title)s</h1><p><i>%(date)s</i></p><p>%(text)s</p>"
        return output % news_to_show[0]
    else:
        abort(404)




if __name__ == "__main__":
    app.run(debug=True)
