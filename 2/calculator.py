#!/usr/bin/python
# -*- coding: UTF-8 -*-

def calculator(text):
    op_order = "+-*/"
    for op in op_order:
        if op == "+":
            result = 0
        terms_list = list(filter(None,text.split(op)))
        print(terms_list)
        if not terms_list:
            return 0
        elif len(terms_list) == 1:
            return (float(terms_list[0]))
        else:
            for term in terms_list:
                if op == "+":
                    result += calculator(term)
                    
                    
                    