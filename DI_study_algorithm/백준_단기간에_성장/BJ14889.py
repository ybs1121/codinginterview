n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)

# chk = [False] * n
# kind = []
# tmp = []

#
# def recur(num):
#
#     if num == n:
#
#         kind.append(tmp)
#         return
#
#     for i in range(n):
#         if chk[i] == False:
#             chk[i] = True
#             tmp.append(i)
#             recur(num+1)
#             chk[i] = False
#             tmp.pop()
#
# recur(0)

tmp =[i for i in range(n)]


from itertools import permutations

min_num = 1000
for i in permutations(tmp,n):
    team_a = i[0:n//2]
    team_b = i[n//2:]
    a = 0
    b = 0
    for j in team_a:
        for k in team_a:
            a += graph[j][k]
    for j in team_b:
        for k in team_b:
            b += graph[j][k]

    tmp_num = abs(a - b)

    min_num = min(min_num, tmp_num)

print(min_num)




