[Click Here to Try the Question](https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem?h_r=internal-search)

```Python
# display each players place on the rank table after each game !!!! idea is great

# rewrite the list to see the max_e occurenced way
def delete_nth(order,max_e):
    if not order or max_e < 1:
        return []

    counted_order = { x:0 for x in order }
    new_order = []

    for item in order:
        if counted_order[item] < max_e:
            counted_order[item] += 1
            new_order.append(item)

    return new_order

ranked = [100,90,90,80,75,60]
player = [50 ,65 ,77 ,90 ,102]

result = []
for i in range(0,len(player)):
    ranked.append(player[i])
    ranked.sort(reverse = True)
    result.append(delete_nth(ranked,1).index(player[i])+1)

print(result)

```
