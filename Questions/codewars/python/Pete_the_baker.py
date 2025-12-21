# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:50:45 2021

@author: Ahmet Kasım Erbay
"""
def min_list(L):

    mini = L[0]

    for i in L:
        if i < mini:
            mini = i

    return mini

def cakes(recipe, available):
    a  = set(recipe.keys())
    b = set(available.keys())

    n_cakes = []

    if a.difference(b)  == set():

        for key,value in recipe.items():
            n_cakes.append(int(available[key]/recipe[key]))

    if len(n_cakes) != 0:
        return min_list(n_cakes)
    else:
        return 0
    
recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}

print(cakes(recipe, available))
