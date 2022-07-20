import sys
input = sys.stdin.readline


n, k = map(int,input().split())

coins = []
count = 0

dp = [0] * (k + 1)
dp[0] = 1

for i in range(n):
    coins.append(int(input()))

for i in coins:
    for j in range(i,k + 1):
        if j - i >= 0:
            dp[j] += dp[j - i]



print(dp[k])

