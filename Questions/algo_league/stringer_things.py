# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:18:27 2021

@author: HP
"""

size = int(input())

stringer_string = input()

stringer_list = list(stringer_string) + [1]

answer = "".join([stringer_list[i]  for i in range(size) if(stringer_list[i] != stringer_list[i+1])])

print(answer)
