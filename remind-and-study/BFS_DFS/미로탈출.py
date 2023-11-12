import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, input())) for _ in range(n)]

# 마지막에 도착하면
nx = [0, 1, 0, -1]
ny = [1, 0, -1, 0]

res = 0

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# def bfs(arr, x, y, res):
#     arr[x][y] = 0
#     # print(res)
#     if x == n - 1 and y == m - 1:
#         print(res + 1)
#         return res
#     for i in range(4):
#         if 0 <= x + nx[i] < n and 0 <= y + ny[i] < m:
#             dx = x + nx[i]
#             dy = y + ny[i]
#             if arr[dx][dy] == 1:
#                 bfs(arr,dx, dy, res + 1)
#
#
# bfs(arr,0,0,0)


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 > dx or n <= dx or 0 > dy or m <= dy:
                continue
            if arr[dx][dy] == 0:
                continue
            if arr[dx][dy] == 1:
                arr[dx][dy] = arr[x][y] + 1
                queue.append((dx,dy))
    return arr[n-1][m-1]

print(bfs(0,0))