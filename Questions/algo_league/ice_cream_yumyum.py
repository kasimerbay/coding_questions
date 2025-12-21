n = int(input())
a = [int(x) for x in input().split(' ')]

a.sort()

answer = 0

for i in range(1,len(a)):
    answer += a[i]

print(answer)