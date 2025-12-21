[Visit The Question!](https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=internal-search)

```python
def divisibleSumPairs(n, k, ar):
    
    sum = 0
    
    for i in range(n-1):
        for j in range(i+1,n):
            if (ar[i] + ar[j])%k == 0:
                sum+=1
    return sum

n = 6
k = 5
ar = [1,3,2,6,1,2]

print(divisibleSumPairs(n,k,ar))

```
