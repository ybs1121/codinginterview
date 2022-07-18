from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().rstrip())))
visited = [[False] * m for _ in range(n)]


q = deque()
q.append((0,0,1))

dx = [1, 0, -1, 0]
dy = [0, 1, 0 ,-1]

list_count = []

while q:

    x,y,count = q.popleft()
    visited[x][y] = True

    if x == n - 1 and y == m - 1:
        list_count.append(count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] == 1:
            q.append((nx,ny,count + 1))

print(min(list_count))