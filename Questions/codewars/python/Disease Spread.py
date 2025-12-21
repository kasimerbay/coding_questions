# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 23:01:28 2021

@author: Ahmet Kasım Erbay
"""
tm = 14
n = 336
s0 = 996
i0 = 2
b = 0.00206
a = 0.41



def epidemic(tm, n, s0, i0, b, a):
    
    r0 = 0
    dt = tm/n
    
    S = [s0]
    I = [i0]
    R = [r0]

    for i in range(n):

        S.append(S[i] - dt * b * S[i] * I[i])
        I.append(I[i] + dt * (b * S[i] * I[i] - a * I[i]))
        R.append(R[i] + dt * I[i] * a)

    return max(I)

print(epidemic(tm, n, s0, i0, b, a)) # < 1

