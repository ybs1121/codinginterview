import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

maps = []

for i in range(n):
    tmp = list(map(int,input().split()))
    maps.append(tmp)

virus = []
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            virus.append([i,j])


nx = [1,0,-1,0]
ny = [0,1,0,-1]
answer = []

def bfs(maps,wall):
    virus = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                virus.append([i, j])
    q = deque()
    q.append((n,m))

    if wall < 3:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    maps[i][j] = 1
                    bfs(maps, wall + 1)
                    maps[i][j] = 0

        print(wall)

        return




## 여기로 넘어오면 wall = 3

    virus = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                virus.append([i, j])

    while virus:
        x,y = virus.popleft()
        for i in range(4):
            xx = nx[i] + x
            yy = ny[i] + y
            if 0 <= xx < n and 0 <= yy < m and maps[xx][yy] == 0:
                virus.append([xx,yy])
                maps[x][y] = 2


    count = 0

    if wall == 3:
        for i in range(n):
            for j in range(m):
                if maps[i][j] == 0:
                    count += 1

        answer.append(count)
        print(maps)

    return




for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            maps[i][j] = 1
            bfs(maps,1)
            maps[i][j] = 0

print(len(answer))
print(max(answer))