#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import locale


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
print(datetime.datetime.now().strftime('%A %d %B %Y'))
print((datetime.datetime.now() - datetime.timedelta(1)).strftime('%A %d %B %Y'))
print((datetime.datetime.now() - datetime.timedelta(1)).strftime('%A %d %B %Y %H:%M'))
print((datetime.datetime.now() - datetime.timedelta(days=31)).strftime('%A %d '
                                                                      '%B %Y %H:%M'))
print(datetime.datetime.strptime("01/01/17 12:10:03.234567", "%m/%d/%y "
                                                             "%H:%M:%S.%f"))