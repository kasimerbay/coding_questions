# # -*- coding: utf-8 -*-
# """
# Created on Fri Aug 13 11:00:47 2021

# @author: Ahmet Kasım Erbay
# """
def gcd_list(l):
    def find_gcd(x, y):

        while(y):
            x, y = y, x % y
        return x

    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i])
    return gcd

def check_all_the_same(liste):

    a = liste[0]

    for i in liste:
        if i!=a:
            return False
        return True

def number_of_divisor(num,div):
    count = 0

    while num%div == 0:

        count += 1
        num = int(num/div)

    return count

def distinct_prime_factors(num):

    from math import sqrt
    factors = []

    if num % 2 == 0:
        factors.append(2)

        while num % 2 == 0:
            num /= 2

    for i in range(3,int(sqrt(num))+1,2):
        if num % i == 0:
            factors.append(i)

            while num % i == 0:
                num /= i
    if num > 2:
        factors.append(int(num))

    return factors

def to_dict(liste,num):
    return {i:number_of_divisor(num, i) for i in liste}

def isPP(num):
    factors = to_dict(distinct_prime_factors(num),num)

    number_of_divisors = len(distinct_prime_factors(num))

    values = []

    keys = []

    for key,value in factors.items():
        keys.append(key)
        values.append(value)


    for key,value in factors.items():

        if number_of_divisors == 1 and value != 1:
            return ( [key,value] )

        elif check_all_the_same(values) and 1 not in values:
            gcd_values = gcd_list(values)
            result = dict()

            key = 1
            value = 0


            for i in range(len(keys)):
                key *= keys[i]**(values[i]/gcd_values)
            result[int(key)] = gcd_values

            for i,j in result.items():
                return ([i,j])

        else:
            return (None)

num =  5111

print(isPP(num))

def gcd_list(l):
    def find_gcd(x, y):

        while(y):
            x, y = y, x % y
        return x

    num1 = l[0]
    num2 = l[1]
    gcd = find_gcd(num1, num2)

    for i in range(2, len(l)):
        gcd = find_gcd(gcd, l[i])
    return gcd

def check_all_the_same(liste):

    a = liste[0]

    for i in liste:
        if i!=a:
            return False
        return True

def number_of_divisor(num,div):
    count = 0

    while num%div == 0:

        count += 1
        num = int(num/div)

    return count

def distinct_prime_factors(num):

    from math import sqrt
    factors = []

    if num % 2 == 0:
        factors.append(2)

        while num % 2 == 0:
            num /= 2

    for i in range(3,int(sqrt(num))+1,2):
        if num % i == 0:
            factors.append(i)

            while num % i == 0:
                num /= i
    if num > 2:
        factors.append(int(num))

    return factors

def to_dict(liste,num):
    return {i:number_of_divisor(num, i) for i in liste}re
