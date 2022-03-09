import sys

input = sys.stdin.readline

num,money = map(int,input().split())

kind = []

for i in range(num):
    kind.append(int(input()))



count = 0
idx = num - 1
while money != 0:
    count += money//kind[idx]
    money = money % kind[idx]
    idx -= 1

print(count)



