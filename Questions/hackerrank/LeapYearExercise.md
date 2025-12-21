[Try the Question](https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=internal-search)
```Python
#Gregorian_Julian_LeapY-> find leap year divisible by 4 not 100

def Gregorian_Julian_LeapY(a):
    G = []
    J = []
    for i in range(1699,a+1):
        if i//4 < (i+1)//4:
            G.append(i+1)
            J.append(i+1)
        if i//100 < (i+1)//100:
            G.remove(i+1)
           
        if i//400 < (i+1)//400:
            G.append(i+1)
    return G,J

G,J = Gregorian_Julian_LeapY(2000)

def dayOfProgrammer(year):
    G,J = Gregorian_Julian_LeapY(year)
    
    if year>1918:
        if year in G:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    elif year < 1918:
        if year in J:
            return "12.09." + str(year)
        else:
            return "13.09." + str(year)
    elif year == 1918:
        return "26.09.1918"

print(dayOfProgrammer(int(input("Enter a year greater than 1700:"))))
```
