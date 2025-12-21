# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 11:10:58 2021

@author: Ahmet Kasım Erbay
"""
### First Solution
        
string = "How can mirrors be real if our eyes aren't real"

new_list = " ".join([i.capitalize() for i in string.split()])

print(new_list)


### Second Sol.

def to_jaden_case(string):
    
    string = string.split()
    
    new_list = []
    
    
    for i in string:
        new_list.append(i[0])
        new_list.append(i[1:])
        
    for i in range(len(new_list)):
        if i%2 == 0:
            new_list[i] = new_list[i].upper()
            # print(new_list[i])
            
    result = []    
    for i in range(len(new_list)):
        if i%2 == 0:
            a = new_list[i] + new_list[i+1]
            result.append(a)
    
    return (" ".join(result))

to_jaden_case(string)