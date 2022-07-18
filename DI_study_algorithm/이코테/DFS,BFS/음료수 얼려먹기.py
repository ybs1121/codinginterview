from collections import deque

import sys
input = sys.stdin.readline



n, m = map(int,input().split())
graphs = []

for i in range(n):
    tmp = input().rstrip()
    tmp = list(tmp)
    graphs.append(tmp)
visited = [[False] * m for _ in range(n)]

count = 0

q = deque()
q.append((0,0))

nx = [1,0,-1,0]
ny = [0,1,0,-1]

def bfs(x,y):

    if visited[x][y] or graphs[x][y] == '1':
        return
    global count
    count += 1
    q = deque()
    q.append((x, y))

    while q:
        x,y = q.popleft()
        visited[x][y] = True

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < n and 0 <= dy < m and not visited[dx][dy] and graphs[x][y] == '0':
                q.append((dx,dy))


for i in range(n):
    for j in range(m):
        bfs(i,j)
print(count)

