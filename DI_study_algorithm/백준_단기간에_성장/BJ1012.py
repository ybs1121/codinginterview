import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
field= []


def bfs(field,visited,x,y ,max_x,max_y):
    if visited[x][y] == 0:
        return False

    visited[x][y] = 0
    q = deque()
    q.append((x,y))
    nx = [1,0,-1,0]
    ny = [0,-1,0,1]

    while q:
        x,y = q.popleft()

        for i in range(4):
            if 0<= x+ nx[i] < max_x and 0 <= y+ ny[i] < max_y:
                if visited[x+ nx[i]][y+ ny[i]] == 1:
                    q.append((x+ nx[i], y+ ny[i]))
                    visited[x+ nx[i]][y+ ny[i]] = 0
    return True











for case in range(t):
    row,col,c = map(int,input().split())

    tmp = [[0]* row for _ in range(col)]
    visited = tmp.copy()

    field.append(tmp)
    for i in range(c):
        y,x = map(int,input().split())
        field[case][x][y] = 1
    count = 0
    for i in range(col):
        for j in range(row):
            if bfs(field,visited,i,j,col,row):
                count += 1
    print(count)







