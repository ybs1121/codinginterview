import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int,input().split())
dishes = []
for i in range(n):
    dishes.append(int(input()))

dishes.extend(dishes)

eat = defaultdict(int)

start = 0
eat[c] += 1

answer = 0


for i in range(len(dishes)):
    eat[dishes[i]] += 1

    if i >= k - 1:
        answer = max(answer, len(eat))

        eat[dishes[start]] -= 1

        if eat[dishes[start]] == 0:
            del eat[dishes[start]]

        start += 1

print(answer)