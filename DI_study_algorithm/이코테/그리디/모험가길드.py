import sys
input = sys.stdin.readline

n = int(input())
group = list(map(int,input().split()))

c = 0
tmp = []
for i in range(n):
    tmp.append(group[i])
    if max(tmp) == len(tmp):
        c += 1
        tmp = []


print(c)

n = int(input())
group = list(map(int,input().split()))
group.sort()
result = 0
count = 0

for i in group:
    count += 1
    if count >= i:
        result += 1
        count = 0

print(result)
