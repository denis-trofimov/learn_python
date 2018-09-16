#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os

# print(os.path.realpath())
name = 'referat.txt'
with open(name, 'r') as file:
    text = file.read()
    print(len(text))
    print(len(text.split()))
    new_text = text.replace('.', '!')
    new_name = 'referat2.txt'
    with open(new_name, 'w') as new_file:
        new_file.write(new_text)
    