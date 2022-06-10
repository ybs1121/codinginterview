import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int,input().split())

dishes = []

for i in range(n):
    dishes.append(int(input()))

dishes.extend(dishes)
left = 0
answer = 0
eat = defaultdict(int)

eat[c] += 1

for right in range(len(dishes)):
    eat[dishes[right]] += 1

    if right >= k-1:
        answer = max(answer,len(eat))
        eat[dishes[left]] -= 1
        if eat[dishes[left]] == 0:
            del eat[dishes[left]]

        left += 1

print(answer)
