from itertools import product

n, k =  map(int,input().split())

nums = []
for i in range(0,n+1):
    nums.append(i)

count = 0
tmp = []
for i in product(nums, repeat = k):
    if sum(i) == 4:
        count += 1
        tmp.append(i)



print(count%1000000000)




n, k = map(int,input().split())
mod = 1000000000
dp = [[0]*(n+1) for _ in range(k+1)]
dp[0][0] = 1
for i in range(1, k+1):
    for j in range(n+1):
        for l in range(j+1):
            dp[i][j] += dp[i-1][j-l]
        dp[i][j] %= mod
print(dp[k][n])