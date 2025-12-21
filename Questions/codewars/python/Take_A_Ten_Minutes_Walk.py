# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:05:04 2021

@author: Ahmet Kasım Erbay
"""

def is_valid_walk(walk):
    
    labels = ["n", "s", "e", "w"]
    
    liste = {i:walk.count(i) for i in labels}
    
    result = True
    
    if liste["n"] == liste["s"] and liste["e"] == liste["w"] and len(walk) == 10:
        
        result = True
    else:
        result = False

    return result

        
walk = ['n','s','n','s','n','s','n','s','n','s']

is_valid_walk(walk)
