import sys
from collections import deque

input = sys.stdin.readline
n, l, r = map(int, input().split())
maps = []
visited = [[False] * n for _ in range(n)]
for i in range(n):
    maps.append(list(map(int, input().split())))

nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
def bfs(x, y):
    q = deque()
    q.append([x, y])
    near_country = [[x, y]]


    while q:
        x, y = q.popleft()
        for i in range(4):
            zx = x + nx[i]
            zy = y + ny[i]
            if 0 <= zx < n and 0 <= zy < n and visited[zx][zy] == False:
                if l <= abs(maps[x][y] - maps[zx][zy]) <= r:
                    visited[zx][zy] = True
                    q.append([zx, zy])
                    near_country.append([zx, zy])


    return near_country


answer = 0

while True:
    move = False
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                near_country = bfs(i, j)
                if len(near_country) > 1:
                    population = sum([maps[x][y] for x, y in near_country]) // len(near_country)
                    move = True
                    for x,y in near_country:
                        maps[x][y] = population

    if not move:
        break
    answer += 1

print(answer)
