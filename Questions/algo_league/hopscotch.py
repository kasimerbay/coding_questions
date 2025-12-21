# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 12:17:56 2021

@author: HP
"""

#%%
def print_matrix(matrix):

    for i in range(len(matrix)):
        if i == len(matrix) - 1:
            print(matrix[i], end="")
        else:
            print(matrix[i],end=" ")

def create_path(n):

    path = []

    for i in range(int(n/2)):
        path.append([3*i + 1])
        path.append([3*i + 2,3*i + 3])

    if n%2 == 1:
        path.append([3*(n//2) + 1])

    return path



a = [int(x) for x in input().split(' ')]

n = a[0]
k = a[1]

result = []

path = create_path(n)
print(path)

# Ters çevirme işlemi
result += path

path.reverse()

result += path[1:]

result = result[:len(result)-1]
print(result)

if ((k/n)%2 and k>n):
    print_matrix(result[(k%(2*n-2) - 1)])

else:
    print_matrix(result[k%(2*n-2) - 1])
#%%

def recursion(n,k):

    if k <= n:
        num = int((3*k-1)/2)
 
        if k%2 == 0:
            print(f"{num} {num + 1}")
        else:
            print(num)

    else:

        if (k <= (2*n - 2)):
            k = 2*n - k
            recursion(k,n)
 
        else:
            if k % (2*n -2) != 0:
                k = k % (2*n - 2)
            else:
                if n != 2:
                    print("Buradayım")
                    k = k % (2*n - 2) + 2
                else:
                    k = 2
            recursion(k,n)

recursion(6,20)





#%%

def oscillator(alist, k):
    n = len(alist)
    for i in range(k):
        j = i%n if i//n % 2 == 0 else n - i%n - 2
        yield alist[j]



l = list(range(1, 7))
k = 20
print(list(oscillator(l, k)))






















