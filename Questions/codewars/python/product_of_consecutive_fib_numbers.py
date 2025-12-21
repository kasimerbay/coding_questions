# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:01:51 2021

@author: Ahmet Kasım Erbay
"""

def fibo(n): # returns nth fibo #
    a, b = 0, 1
    while n >= 0:
        n -= 1
        a,b = b ,a+b
    return a

def productFib(prod):
    
    i = 0
    a = fibo(i)*fibo(i+1)
    
    while a <= prod:
        a = fibo(i)*fibo(i+1)
        
        print(a,fibo(i),fibo(i+1))
        
        if a == prod:
            return [fibo(i), fibo(i+1), True]
        elif a>prod:
            return [fibo(i), fibo(i+1), False]
        i += 1

prod = 0
print(productFib(prod))










