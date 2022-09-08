import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())

dic = {}

for i in range(n - 1):
    edge1, edge2 = map(int,input().split())

    if edge1 in dic:
        dic[edge1].append(edge2)
    else:
        dic[edge1] = [edge2]

    if edge2 in dic:
        dic[edge2].append(edge1)
    else:
        dic[edge2] = [edge1]

answer = 0

nodes = [i for i in range(1,n+1)]

dp = [[0] * (n + 1) for _ in range(n + 1)]

dp = [0] * (n + 1)

while True:
    answer += 1

    chk = False

    if answer == 1:
        for i in range(1,n+1):
            dp[i] = len(dic[i])

            if dp[i] == n - 1:
                chk = True
    else:
        tmp_dp = list(dp)

        for i in range(1,n+1):
            for j in range(1,n+1):
                if i == j:
                    continue
                dp[i] = max(dp[i],tmp_dp[i] + len(dic[j]))

                if dp[i] == n - 1:
                    chk = True
    #
    # if answer == 1:
    #     for i in range(1,n+1):
    #         dp[answer][i] = len(dic[i])
    #         if dp[answer][i] == n - 1:
    #             chk = True
    #
    # else:
    #     for i in range(1,n+1):
    #         for j in range(1, n+1):
    #             if j == i:
    #                 continue
    #
    #             dp[answer][i] = max(dp[answer][i], dp[answer - 1][i] + len(dic[j]))
    #
    #             if dp[answer][i] == n - 1:
    #                 chk = True


    if chk:
        break


print(answer)





