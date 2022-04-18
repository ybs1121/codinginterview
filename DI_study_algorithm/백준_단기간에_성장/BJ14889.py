n = int(input())
graph = []
for i in range(n):
    tmp = list(map(int,input().split()))
    graph.append(tmp)
#
# chk = [False] * n
#
# min_num = 9999
#
# tmp =[]
# kind = []
# def recur(num):
#     global min_num
#
#     if num == n:
#         team_a = tmp[0:num//2]
#         team_b = tmp[num//2:]
#         kind.append(tmp[:])
#         a = 0
#         b = 0
#         for j in team_a:
#             for k in team_a:
#                 a += graph[j][k]
#
#         for j in team_b:
#             for k in team_b:
#                 b += graph[j][k]
#         min_num = min(min_num,abs(a-b))
#
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
#
# print(min_num)
#
# print(kind)

# tmp =[i for i in range(n)]
#
#
# from itertools import permutations
#
# min_num = 1000
# for i in permutations(tmp,n):
#     team_a = i[0:n//2]
#     team_b = i[n//2:]
#     a = 0
#     b = 0
#     for j in team_a:
#         for k in team_a:
#             a += graph[j][k]
#     for j in team_b:
#         for k in team_b:
#             b += graph[j][k]
#
#     tmp_num = abs(a - b)
#
#     min_num = min(min_num, tmp_num)
#
# print(min_num)

import itertools
arr = [i for i in range(n)]
cases = list(itertools.combinations(arr, int(n//2)))

min_value = 10000
for case_a in cases:
	stat_A = 0
	stat_B = 0
	for x in case_a:
		for y in case_a:
			stat_A += graph[x][y]
	case_b = [x for x in range(n) if x not in case_a]
	for x in case_b:
		for y in case_b:
			stat_B += graph[x][y]
	min_value = min(min_value, abs(stat_A-stat_B))
print(min_value)





