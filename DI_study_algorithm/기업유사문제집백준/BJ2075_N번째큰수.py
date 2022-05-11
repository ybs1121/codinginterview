import sys
import heapq
input = sys.stdin.readline
n = int(input().strip())
#matrix = [list(map(int,input().split())) for _ in range(n)]

matrix_extend = []

# for i in matrix:
#     matrix_extend.extend(i)
#
# sort_matrix = sorted(matrix_extend,reverse=True)

# print(sort_matrix[n-1])
# stack = [-1]
# for i in matrix:
#     for j in i:
#
#         tmp = []
#         if stack[-1] < j:
#             while stack:
#
#                 if stack[-1] >= j:
#                     break
#                 else:
#                     tmp.append(stack.pop())
#             stack.append(j)
#             idx = n - len(stack)
#             stack.extend(tmp[:idx])
# print(stack[-1])


stack = [-1]
for i in range(n):
    for j in list(map(int,input().split())):
        tmp = []
        while stack and stack[-1] < j:
            tmp.append(stack.pop())

        stack.append(j)
        stack.extend(tmp)

        if len(stack) > n:
            stack = stack[:n]


print(stack[-1])

heap = []
for i in range(n):
    rows = list(map(int,input().split()))

    if not heap:
        for j in rows:
            heapq.heappush(heap,j)
    else:
        for j in rows:
            if heap[0] < j:
                heapq.heappush(heap,j)
                heapq.heappop(heap)

print(heap[0])



