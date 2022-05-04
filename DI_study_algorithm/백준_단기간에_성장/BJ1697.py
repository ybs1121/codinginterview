x, y = map(int,input().split())

visited = [False] * 100001

from collections import deque
sec = 0

q = deque()
q.append([x,sec])

while q:
    point,sec = q.popleft()
    if point == y:
        print(sec)
        break

    visited[point] = True

    if 0 <= point - 1 <= 100000 and visited[point - 1] == False:
        visited[point - 1] = True
        q.append([point - 1, sec+1])
    if 0 <= point + 1 <= 100000 and  visited[point + 1] == False:
        visited[point + 1] = True
        q.append([point + 1,sec + 1])
    if 0 <= point * 2 <= 100000  and visited[point * 2] == False:
        visited[point*2] = True
        q.append([point * 2,sec+1])