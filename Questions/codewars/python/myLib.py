"""
    A module created for me by me
    
    Filobitmiş
    
    FUNCTIONS
    ---------
        min_list(L)
        distinct_prime_factors(num):
        unique_in_order(iterable):
        number_of_digit(num):
        list_integer(liste):
        next_perfect_square(sq):
        lcm_list(liste)
        lcm(num1, num2)
        gcd_list(l)
        gcd(a,b)
        delete_nth(order,max_e)
        check_negative(seq)
        order_of_power(num,div)
        number_of_divisor(num,div)
        sumList(N)
        mean(N)
        mod(N)
        median(N)
        fib(n)
        primes(a,b)
        isPerfect(l)
        odd_index(seq)
        
"""

def min_list(L):
    """

    Parameters
    ----------
    L : list

    Returns
    -------
    mini : int
        -> minimum number in the list

    """

    mini = L[0]

    for i in L:
        if i < mini:
            mini = i

    return mini

def distinct_prime_factors(num):
    """

    Parameters
    ----------
    num : integer

    Returns
    -------
    factors : list of integers
        -> All the distinct pirme factors of "num"

    """

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

def unique_in_order(iterable):
    """

    Parameters
    ----------
    iterable : iterable type object
        random occuranced iterable

    Returns
    -------
    result : list
        -> returns deleted consecutive occurances: "[AAAAABBBBBCCCCCDDDDD] -> [ABCD]"

    """
    if len(iterable) != 0:
    
        result = [iterable[0]]

        for i in range(len(iterable)):
            if iterable[i] != result[len(result)-1]:
                result.append(iterable[i])

    else: result = []

    return result

def number_of_digit(num):
    """

    Parameters
    ----------
    num : int
        integer to be checked

    Returns
    -------
    count : int
        -> # of digits

    """
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count

def list_integer(liste):
    """

    Parameters
    ----------
    liste : list of variables
        any type of varibale

    Returns
    -------
    result : list
        -> returns only a list of integers

    """
    result = []

    for i in liste:
        try:
            if type(i) != int():
                result.append(int(i))
        except:
            continue
    return result

def next_perfect_square(sq):

    """
    Parameters
    ----------
    num : a numbe

    Returns
    -------
    "True" if it is a perfect square or "the perfect square" right after the num

    """
    a = int(sq**(0.5))
    #print(a)
    
    if a*a == sq: 
        return True
    else: 
        return (a+1)

def lcm_list(liste):
    """
    
    Parameters
    ----------
    liste : list of integers
        DESCRIPTION.

    Returns
    -------
    lcm : integer
        -> Returns the least common multiple of the numbers in the list

    """
    
    def lcm(num1, num2):
        if(num1>num2):
            num = num1
            den = num2
        else:
            num = num2
            den = num1
        rem = num % den
        while(rem != 0):
            num = den
            den = rem
            rem = num % den
        gcd = den
        result = int(int(num1 * num2)/int(gcd))
        return result
    
    num1 = liste[0]
    num2 = liste[1]
    
    result = lcm(num1, num2)
    
    for i in range(2, len(liste)):
        result = lcm(lcm, liste[i])
    return result

def lcm(num1, num2):
    """

    Parameters
    ----------
    num1 : int
    num2 : int

    Returns
    -------
    lcm : int
        -> least common multiple of num1 and num2

    """
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm

def gcd_list(l):
    """

    Parameters
    ----------
    l : list
        list of integers

    Returns
    -------
    int
        -> GCD of the numbers in the list

    """
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

def gcd(a,b):
    """
    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    TYPE : integer
        
    -> The greatest common divisor of the pair (a,b)
        
    """
    
    if(a==0):
        return b
    else:
        return gcd(b%a,a)

def delete_nth(order,max_e):
    """
    

    Parameters
    ----------
    order : the sequence of numbers
    max_e : integer
        maximum occurance of a number in the list

    Returns
    -------
    list
        list of numbers has the max desired occurance

    """
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order

def check_negative(seq):
    """

    Parameters
    ----------
    seq : list of integers

    Returns
    -------
    bool
        True: if there is a negative number in the list
        False: otherwise

    """
    for i in seq:
        if i < 0:
            return True
    return False

def order_of_power(num,div):
    """
    Parameters
    ----------
    num : int
        
    div : int

    Returns
    -------
    count : int
        -> returns how many times "div" divides "num"

    """
    count = 0
    while num%div == 0:
        count += 1
        num = int(num/div)
    return count

def number_of_divisor(num,div):
    """

        Parameters
        ----------
        num : integer
            the number to be divided by "div".
        div : integer
            the number to divide. It must be divide by num%div == 0
    
        Returns
        -------
        -> [div,count]: the integer and its power count "8 -> [2,3] = 2^3"

    """
    divisors = dict()
    
    for i in div:
        count = 0
        while num%i == 0:
            count += 1
            
            num = int(num/i)
        divisors.update({i:count})
    
    return divisors

def CaesarEncoder(txt,key):
    
    alphabet = 'aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ'
    txt1 = ""
    a = " "
    for i in txt:
        if(i == a):
            txt1 = txt1 + a
        else:
            loc = -1
            for j in alphabet:
                loc +=1
                if(i == j and loc%2 == 1):

                    txt1 = txt1 + alphabet[(loc+2*int(key))%58]
                elif(i == j and loc%2 == 0):
                    txt1 = txt1 + alphabet[(loc+2*int(key))%58]
    
    return txt1

def CaesarDecoder(txt,key):
    
    alphabet = 'aAbBcCçÇdDeEfFgGğĞhHıIiİjJkKlLmMnNoOöÖpPrRsSşŞtTuUüÜvVyYzZ'
    txt1 = ""
    a = " "
    for i in txt:
        if(i == a):
            txt1 = txt1 + a
        else:
            loc = -1
            for j in alphabet:
                loc +=1
                if(i == j and loc%2 == 1):

                    txt1 = txt1 + alphabet[(loc-2*int(key))%58]
                elif(i == j and loc%2 == 0):
                    txt1 = txt1 + alphabet[(loc-2*int(key))%58]
    
    return txt1

def EncodeCaesar(text,key):
    a=ord('a')
    alph=[chr(i) for i in range(a,a+26)]
    text = text.lower().split()
    enc_word=""
    for elements in text:
        for letters in elements :
            letter_index = alph.index(letters)
            letter_index += (int(key))%26
            enc_word =enc_word + alph[letter_index%26]
        enc_word = enc_word + " "
    return (enc_word.rstrip(" "))

def DecodeCaesar(text,key):
    a=ord('a')
    alph=[chr(i) for i in range(a,a+26)]
    text = text.lower().split()
    enc_word=""
    for elements in text:
        for letters in elements :
            letter_index = alph.index(letters)
            letter_index += 26-(int(key))%26
            enc_word =enc_word + alph[letter_index]
        enc_word = enc_word + " "
    return (enc_word.rstrip(" "))

def sumList(N):
    """
    

    Parameters
    ----------
    N : list of  numbers that are INTEGER or STRING

    Returns
    -------
    s : INTEGER
    
    -> sum of the numbers

    """
    s = 0
    for i in N:
        s+=int(i)
    return s

def mean(N):
    return sumList(N)/len(N)

def median(N):
    if(len(N)%2==1):
        return int(len(N)/2)
    else:
        L = []
        L.append(N[int(len(N)/2)])
        L.append(N[int(len(N)/2)-1])
        return mean(L)

def mod(N):
    """
    

    Parameters
    ----------
    N : list of numbers.

    Returns
    -------
    elt : integer
    
    -> returns the integer which has the max occurance in the list
    """
    freq = N.count(N[0])
    elt = N[0]
    for i in N:
        if(N.count(i)>freq):
            freq = N.count(i)
            elt = i
    return elt

def fib(n):
    """
    

    Parameters
    ----------
    n : integer.

    Returns
    -------
    result : list.
    
    -> return Fibonacci series up to n

    """
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def primes(a,b):
    """
    

    Parameters
    ----------
    a : integer
    b : integer

    Returns
    -------
    prime : list
    
    -> The list of all the prime numbers between a,b inclusive.
        

    """
    l = [i for i in range(a,b+1)]
    prime = []
    for i in l:
        t = [k for k in range(2,i)]
        if(i>1):
            for j in t:
                if(i%j == 0):
                    break
            else:
                prime.append(i)
    return prime

def isPerfect(l):

    """
    

    Parameters
    ----------
    l : integer

    Returns
    -------
    bool
        -> check if the number is a perfect number

    """
    #check if the number is a perfect number
    sum = 0
    div = list()
    for i in range(1,l):
        if(l%i == 0):
            div.append(i)
            
    for i in div:
        sum += i
    if(sum == l):
        return True
    else:
        return False

def odd_index(seq):
    """

    Parameters
    ----------
    seq : list
        integer list

    Returns
    -------
    integer
        index of the number in the list that has odd number of occurance

    """
    
    freq = [0]*(max(seq)+1)
    for i in seq:
        freq[i] += 1
            
    for i in freq:
        if i % 2 == 1:
            return freq.index(i)