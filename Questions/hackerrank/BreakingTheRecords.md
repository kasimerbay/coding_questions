[Visit The Question](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem)
```Python

# How many times you exceed the thresholds both up and down in a list

def breakingRecords(scores):
    a = []
    a.append(scores[0])
    
    sumin = 0
    sumax = 0
    
    for i in range(1,len(scores)):
        if scores[i]<min(a):
            a.append(scores[i])
            sumin+=1
        elif scores[i]>max(a):
            a.append(scores[i])
            sumax+=1
    print(sumax,sumin)

#scores = [10,5,20,20,4,5,2,25,1] #try this list too.

scores = [3,4,21,36,10,28,35,5,24,42]


breakingRecords(scores)
```
