# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 23:32:15 2021

@author: Ahmet Kasım Erbay
"""

liste = [1,2,'a','b']

def filter_list(liste):
    result = []

    for i in liste:
        try:
            if type(i) != int():
                result.append(int(i))
        except:
            continue
    return result

print(filter_list(liste))