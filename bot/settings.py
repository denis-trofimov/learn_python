#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


TELEGRAM_API_KEY = os.environ.get('TELEGRAM_API_KEY')
CLARIFAI_API_KEY = os.environ.get('CLARIFAI_API_KEY')
# Настройки прокси
PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}
}
