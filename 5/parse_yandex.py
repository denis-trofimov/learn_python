#!/usr/bin/python3
# -*- coding: UTF-8 -*-
u""" Другая частая задача, с которой приходится сталкиваться - это получение
    данных с чужих сайтом. Не у всех сайтов есть api, поэтому нужно уметь
    получить html и добыть из него нужные данные:

    Получение html-страницы при помощи requests
    Основы библиотеки Beautiful Soup
    Разбираем поисковую страницы Яндекса

"""
import requests
import pprint
from bs4 import BeautifulSoup


def get_page(url):
    try:
        params = {}
        responce = requests.get(url, params=params)
        responce.raise_for_status()
        print(responce.apparent_encoding)
        return responce.text
    except requests.exceptions.RequestException as e:
        print(e)
        return None


def parse_page(data):
    bs = BeautifulSoup(data, 'html.parser')
    sites_list = []
#    print(bs.prettify)
    for item in bs.find_all('li', class_='serp-item'):
        title = item.find('div', class_='organic__url-text').text
        link = item.find('a', class_='path__item').get('href')
        sites_list.append({'link': link, 'title': title})
    return sites_list


if __name__ == '__main__':
    url = "https://yandex.ru/search/?lr=213&text=python"
#    url = 'https://learn.python.ru/lessons/5_db.html?full#0'
    data = get_page(url)
    if data:
        sites_list = parse_page(data)
        pprint.pprint(sites_list)
