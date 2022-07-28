from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))


answer = 0
q = deque()
# 0 -> 가로 / 1 -> 세로 /2 -> 대각선
q.append((0, 1, 0))

while q:

    x, y, d = q.popleft()

    if x == n - 1 and y == n - 1:
        answer += 1
        continue

    if d == 0 or d == 2:
        if 0 <= y + 1 < n and maps[x][y + 1] == 0:
            q.append((x, y+1, 0))

    if d == 1 or d == 2:
        if 0 <= x + 1 < n and maps[x + 1][y] == 0:
            q.append((x + 1, y, 1))

    if d == 0 or d == 1 or d == 2:
        if 0 <= x + 1 < n and 0 <= y + 1 < n and maps[x][y + 1] == 0 and maps[x + 1][y] == 0 and maps[x + 1][y + 1] == 0:
            q.append((x + 1, y + 1, 2))


print(answer)


import sys
input = sys.stdin.readline

n = int(input())
maps = []

for i in range(n):
    maps.append(list(map(int, input().split())))


answer = 0
# 0 -> 가로 / 1 -> 세로 /2 -> 대각선

def dfs(x, y, d):
    global answer

    if (x, y) == (n - 1, n - 1):
        answer += 1
        return

    if d == 0 or d == 2:
        if 0 <= y + 1 < n and maps[x][y + 1] == 0:
            dfs(x,y+1,0)

    if d == 1 or d == 2:
        if 0 <= x + 1 < n and maps[x + 1][y] == 0:
            dfs(x + 1, y, 1)

    if d == 0 or d == 1 or d == 2:
        if 0 <= x + 1 < n and 0 <= y + 1 < n and maps[x][y + 1] == 0 and maps[x + 1][y] == 0 and maps[x + 1][y + 1] == 0:
            dfs(x + 1, y + 1, 2)

dfs(0, 1, 0)
print(answer)

