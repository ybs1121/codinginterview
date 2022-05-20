import sys

input = sys.stdin.readline

a,b = map(int,input().split())
dp = [0,1,2,4]
num = 4
for i in range(4,b+1):
    n = i // 4
    if i % 4 == 3:
        num = num + n + 1

    else:
        num = num + n




print(num)
