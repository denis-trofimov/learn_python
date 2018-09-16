#!/usr/bin/python
# -*- coding: UTF-8 -*-

import csv


user_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
fieldnames = user_list[0].keys()

with open("ab.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(user_list)
    
with open("user_list.csv", 'w') as file:
    writer = csv.DictWriter(file, fieldnames, dialect='excel')
    writer.writeheader()
    writer.writerows(user_list)