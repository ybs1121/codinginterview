import sys
input = sys.stdin.readline


n = int(input())
rs = [0] * 1000

rs[0] = 1
rs[1] = 2
for i in range(2,n):
    rs[i] = rs[i-1] + rs[i-2]

print(rs[n-1]%10007)
