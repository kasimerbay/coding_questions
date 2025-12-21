# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 14:20:57 2021

@author: Ahmet Kasım Erbay
"""

def number_of_digit(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count
def check_all_zeros(liste):
    result = True
    for i in liste:
        if i != "0":
            result = False
    return result
def check_increment(list_right,first_zeros): 
    list_right_right = list_right[first_zeros:]
    if number_of_digit(int("".join(list_right_right)) + 1) > number_of_digit(int("".join(list_right))):
        return True
    return False

def increment_string(string):
    
    string_list = [i for i in string]
    length = len(string_list)
    index = 0
    
    
    if len(string)  == 0 or string[-1].isdigit() == False:
        return (string + str(1))
    else:
        for i in string_list[::-1]:
            try:
                ind = int(i)
                index += 1
            except:
                break
        
        list_left = list(string)[:length - index] # Stringdeki sayılar hariç kısım
        list_right = list(string)[length - index:] # String içerisindeki sonda bulunan sayı kısımları

        count = 0
        first_zeros = len(list_right)
        for i in list_right:
            if int(i) != 0:
                
                first_zeros = list_right.index(i)
                break
            else:
                count += 1
        if check_all_zeros(list_right):
            return ("".join(list_left) + (count - 1) * "0" + str(1))
        elif count == 0:
            return ("".join(list_left) + str(int("".join(list_right))+1))
        else:
            if check_increment(list_right, first_zeros):
                return ("".join(list_left) + (count - 1) * "0" + str(int("".join(list_right))+1))
            else:
                return ("".join(list_left) + count * "0" + str(int("".join(list_right))+1))





































