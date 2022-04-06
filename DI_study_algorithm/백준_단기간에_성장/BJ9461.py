import sys

input = sys.stdin.readline

N = int(input())

list = []
for i in range(N):
    list.append(int(input()))

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1

max_num = max(list)

for j in range(4, max_num+1):
    dp[j] = dp[j-3] + dp[j - 2]

for i in list:
    print(dp[i])









