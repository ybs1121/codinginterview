import sys
input = sys.stdin.readline


n, e = map(int,input().split())

graph = {}


#양뱡향 설정
for i in range(e):
    a,b,c = map(int,input().split())

    if a in graph:
        graph[a].append((b,c))

        if b in graph:
            graph[b].append((a,c))
        else:
            graph[b] = [(a,c)]
    else:
        graph[a] = [(b,c)]
        graph[b] = [(a,c)]

# 반드시 지나야 하는 정점 두 개
first, sec = map(int,input().split())

distance = [sys.maxsize] * n

start = 0
distance[0] = 0




print(graph)


