# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 21:22:55 2021

@author: Ahmet Kasım Erbay
"""

def consecutive(str1,str2):
    if [(str1 == "NORTH" and str2 == "SOUTH") or (str1 == "SOUTH" and str2 == "NORTH")] or [(str1 == "EAST" and str2 == "WEST") or (str1 == "WEST" and str2 == "EAST")]:
        return True

a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]

count = 0

for i in range(len(a)):
    