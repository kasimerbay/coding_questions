# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:29:22 2021

@author: HP
"""

n = int(input())
a = [int(x) for x in input().split(' ') if x != ""]

records = a[0]

answer = 0

for i in range(1, n):
    if (records < a[i]):
        records = a[i]
        answer += 1
        print(records)

print(answer)
