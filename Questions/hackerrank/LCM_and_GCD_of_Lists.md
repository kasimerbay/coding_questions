[Visit The Question](https://www.hackerrank.com/)
```Python
#%% Finding GCD & LCM of A list of numbers!!!!!

# LCM of a list of numbers
def lcm_list(b):
    def find_lcm(num1, num2):
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
    
    num1 = b[0]
    num2 = b[1]
    
    lcm = find_lcm(num1, num2)
    
    for i in range(2, len(b)):
        lcm = find_lcm(lcm, b[i])
    return lcm
# GCD of list of numbers
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

a = [2,6]
b = [24,48]

sum = 0

a.sort()
b.sort()

# make lists if there is only one element in the list to be sure we send lists to the functions above
if len(a) == 1:
    a.append(a[0])
if len(b) == 1:
    b.append(b[0])

# Look the gcd's of the numbers
print(gcd_list(b))
print(gcd_list(a))

c = [i for i in range(a[len(a)-1],gcd_list(b)+1)]

print(c)

# for all elements in list c, if the elements divide sum up
for i in c:
    if gcd_list(b)%(i) == 0 and i%lcm_list(a)==0:
        sum+=1
        print(i)
        
print(sum)
```
