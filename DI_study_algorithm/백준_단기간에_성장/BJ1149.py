import sys
input = sys.stdin.readline

n = int(input())

house = []
for i in range(n):
    tmp = list(map(int,input().split()))
    house.append(tmp)

rgb = [False] * 3
sum = 0
for i in range(1, n):
    house[i][0] += min(house[i-1][1], house[i-1][2])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][0], house[i-1][1])
print(min(house[-1]))

