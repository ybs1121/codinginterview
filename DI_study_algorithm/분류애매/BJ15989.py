import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * 10001

dp[1] = 1
dp[2] = 2
dp[3] = 3


for i in range(4,10001):
    if i % 2 == 0:
        dp[i] = dp[i - 1] + dp[i - 2] - 1
    else:
        dp[i] = dp[i - 1] - 1


for i in range(n):
    inputs = int(input())
    print(dp[inputs])