import sys

input = sys.stdin.readline

N , M , V = map(int,input().split())

graph = [list(map(int,input().split())) for _ in range(M)]
edge = [[] for _ in range(N + 1)]
graph.sort()
count = 0
for i in graph:
    edge[i[0]].append(i[1])
    edge[i[1]].append(i[0])

for i in range(1,len(edge)):
    edge[i].sort()


visited = [False] * (N + 1)

def dfs(visited,V,edge):
    visited[V] = True
    print(V, end= " ")
    for i in edge[V]:
        if visited[i] == False:
            visited[i] = True
            dfs(visited,i,edge)
dfs(visited,V,edge)




visited = [False] * (N + 1)
from collections import deque


def bfs(visited,V,edge):
    queue = deque([V])
    visited[V] = True

    while queue:
        V = queue.popleft()
        print(V, end= " ")
        for i in edge[V]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


print()
bfs(visited,V,edge)


target = 7
list = [1,23,124,7,123,1,1,1,1,1]
for i in range(10):
    if list[i] == target:
        print("Find")







