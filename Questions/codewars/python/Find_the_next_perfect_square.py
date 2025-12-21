# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:48:05 2021

@author: Ahmet Kasım Erbay
"""
def next_perfect_square(sq):
    
    a = int(sq**(0.5))
    #print(a)
    
    if a*a == sq: 
        return True
    else: 
        return (a+1)

sq = 120

print(next_perfect_square(sq))

