# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 23:07:50 2021

@author: Ahmet Kasım Erbay
"""

source_array = [1, 111, 11, 11, 2, 1, 5, 0]

odds = []
odd_indexes = []
index = 0

for i in source_array:
    if i%2 == 1:
        odds.append(i)
        odd_indexes.append(index)
    index += 1

odds.sort()

for element,index in zip(odds,odd_indexes):
    source_array[index] = element
    
print(source_array)































