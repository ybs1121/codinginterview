import sys
input = sys.stdin.readline

n = int(input())

card = list(map(int,input().split()))



money = [0] * n
money[0] = card[0]
money[1] = max(money[0]*2,card[1])
money[2] = max(money[0] + money[1],card[2])

for i in range(3,n):
    money[i] = max(money[i-1]+ money[i-2] - money[i - 3], card[i])


print(money[-1])


N = int(input())
card = [0]
card += list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = card[1]
dp[2] = max(card[2], card[1]*2)

for i in range(3, N+1):
    dp[i] = card[i] #자기 자신으로 만드는 경우
    for j in range(1, i//2 + 1): #j와 i-j로 만드는 경우
        dp[i] = max(dp[i], dp[j] + dp[i-j])

print(dp[N])
