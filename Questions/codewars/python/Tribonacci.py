# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 21:43:48 2021

@author: Ahmet Kasım Erbay
"""

signature = [75, 193, 176]
n = 3

def tribonacci(signature, n):
    if n>=3:
        for i in range(n-3):
            signature.append(signature[i] + signature[i+1] + signature[i+2])
    else:
        for i in range(3-n):
            signature.pop(len(signature) - 1)
    return signature

print(tribonacci(signature, n))