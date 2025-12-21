# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 22:50:53 2021

@author: Ahmet Kasım Erbay
"""

def unique_in_order(iterable):
    if len(iterable) != 0:
    
        result = [iterable[0]]

        for i in range(len(iterable)):
            if iterable[i] != result[len(result)-1]:
                result.append(iterable[i])

    else: result = []

    return result
        
iterable = 'AAAABABBCCDAABBB'

print(unique_in_order(iterable))

#%%

from itertools import groupby

iterable = 'AAAABBBCCDAABBB'

def unique_in_order(iterable):
    return [k for (k, _) in groupby(iterable)]

print(unique_in_order(iterable))

#%%

iterable = 'AAAABBBCCDAABBB'

unique_in_order = lambda l: [z for i, z in enumerate(l) if i == 0 or l[i - 1] != z]

print(unique_in_order(iterable))