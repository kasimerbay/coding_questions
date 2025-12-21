# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 19:40:39 2021

@author: Ahmet Kasım Erbay
"""

word = "WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB"

# word = " ".join(word.replace("WUB", " ").strip().split())
# word = " ".join(word.replace("WU B", " ").strip().split())
# word = " ".join(word.replace("W UB", " ").strip().split())

# print(word)

a = "WUB"
b = "W UB"
c = "WU B"

while True:
    
    if a in word:
        word = word.replace(a, " ")
    elif b in word:
        word = word.replace(b, " ")
    elif c in word:
        word = word.replace(c, " ")
    else:
        break
    
new_word = " ".join(word.strip().split())

print(new_word)

