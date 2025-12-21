# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 10:04:15 2021

@author: HP
"""
from re import search

#regex="^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{6,}$"
regex = "(?=.*?[a-z])(?=.*?[0-9])(?=.*?[A-Z])(^[!@#&()–[{}]:;‘,?/*]).{6,}"

print(bool(search(regex, 'fjd3IR9')))
