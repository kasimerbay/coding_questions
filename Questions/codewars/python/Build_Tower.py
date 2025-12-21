# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 22:34:38 2021

@author: Ahmet Kasım Erbay
"""

def tower_builder(n_floor):
    return [" " * (n_floor - i - 1) + "*" * (2*i + 1) + " " * (n_floor - i - 1) for i in range(n_floor)]

for i in tower_builder(10):
    print(i)

