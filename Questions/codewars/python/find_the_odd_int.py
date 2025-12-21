# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:34:17 2021

@author: Ahmet Kasım Erbay
"""
def delete_nth(order,max_e):
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order


seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

liste = delete_nth(seq, 1)

frequencies = [[i,seq.count(i)] for i in liste]

for i,j in [[i,seq.count(i)] for i in liste]:
    if j%2 == 1:
        print(i)
    
#%%

import operator
from functools import reduce

def find_it(xs):
    return reduce(operator.xor, xs)

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

print(find_it(seq))

#%%
seq = [1, 1, 2, 2, 5, 2, 4, 4, -1, 2, 5]

def check_negative(seq):
    for i in seq:
        if i < 0:
            return True
    return False

def odd_index(seq):
    
    freq = [0]*(max(seq)+1)
    for i in seq:
        freq[i] += 1
            
    for i in freq:
        if i % 2 == 1:
            return freq.index(i)



if check_negative(seq):
    mini = -min(seq)
    seq = [i + mini for i in seq]
    result = odd_index(seq) - mini
else:
    result= odd_index(seq)
    
print(result)
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        