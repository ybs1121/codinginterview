import sys
input = sys.stdin.readline

n = int(input())
sch = []
for i in range(n):
    tmp = list(map(int,input().split()))
    sch.append(tmp)


dp = [0] * (n+1)

for i in range(n-1,-1,-1):
    day = sch[i]
    if i + day[0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], day[1] + dp[i+day[0]])


print(dp[0])



