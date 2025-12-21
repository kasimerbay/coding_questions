# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:21:14 2021

@author: Ahmet Kasım Erbay
"""

sentence = "is2 Thi1s T4est 3a"

sentence = sentence.split()

new_sentence = []

length = [i for i in range(len(sentence))]
    
for i in range(len(length)):
    for j in sentence:
        if str(i+1) in j:
            new_sentence.append(j)

print(" ".join(new_sentence))