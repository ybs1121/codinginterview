import sys
from collections import deque
# 4 5
# 00110
# 00011
# 11111
# 00000
n, m = map(int, sys.stdin.readline().split())
arr = [list(map(int, input())) for _ in range(n)]


def dfs(arr, x, y):
    nx = [1, 0, -1, 0]
    ny = [0, 1, 0, -1]
    arr[x][y] = 1
    for i in range(4):
        if 0 <= x + nx[i] < n and 0 <= y + ny[i] < m:
            dx = x + nx[i]
            dy = y + ny[i]
            if arr[dx][dy] == 0:
                dfs(arr, dx, dy)


res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            print(i,j)
            dfs(arr, i, j)
            res += 1
            print(arr)

print(res)
