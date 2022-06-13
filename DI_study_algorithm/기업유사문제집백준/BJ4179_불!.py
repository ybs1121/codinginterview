import sys
from collections import deque
input = sys.stdin.readline

r,c = map(int,input().split())
maps = []
visited = [[False] * c for _ in range(r)]

for i in range(c):
    tmp = input().rstrip()
    tmp = list(tmp)
    maps.append(tmp)

j_point = (-1,-1)
fire_point = (-1,-1)
escape_point = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'J':
            j_point = (i,j,1)
        if maps[i][j] == 'F':
            fire_point = (i,j)

for i in range(c):
    if maps[0][i] == '.':
        escape_point.append((0,i))
        break
for i in range(c-1,-1,-1):
    if maps[0][i] == '.':
        escape_point.append((0,i))
        break
for i in range(c):
    if maps[r-1][i] == '.':
        escape_point.append((r-1,i))
        break
for i in range(c-1,-1,-1):
    if maps[r-1][i] == '.':
        escape_point.append((r-1,i))
        break

q = deque()
q.append(j_point)

fire_q = deque()
fire_q.append(fire_point)

zx = [1,0,-1,0]
zy = [0,1,0,-1]
answer = []

while q:
    x,y,move = q.popleft()
    visited[x][y] = True
    if (x,y) in escape_point:
        answer.append(move)

    for i in range(4):
        nx = x + zx[i]
        ny = y + zy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] == '.':
            q.append((nx,ny,move + 1))

        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and maps[nx][ny] == '.':
            maps[nx][ny] = 'F'

if answer:
    print(min(answer))
else:
    print("IMPOSSIBLE")



#정답
from sys import stdin
from collections import deque

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
r, c = map(int, stdin.readline().split())
board, res = [], 0

# 지환이와 불난 곳 저장할 변수
F, J = deque(), deque()

for i in range(r):
    data = list(stdin.readline().rstrip())
    for j in range(c):
        if data[j] == 'J':
            J.append((i, j))
        if data[j] == 'F':
            F.append((i, j))

    board.append(data)


def bfs():
    global F, J, res

    while 1:
        res += 1
        temp = []
        while F:
            x, y = F.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if -1 < nx < r and -1 < ny < c:
                    if board[nx][ny] == '.' or board[nx][ny] == '$':
                        temp.append((nx, ny))
                        board[nx][ny] = 'F'
        F = deque(temp)

        temp = []
        while J:
            x, y = J.popleft()
            if x == 0 or y == 0 or x == r - 1 or y == c - 1:
                return res

            for i in range(4):
                nx, ny = dx[i] + x, dy[i] + y
                if -1 < nx < r and -1 < ny < c and board[nx][ny] == '.':
                    temp.append((nx, ny))
                    board[x][y] = '$'
                    board[nx][ny] = 'J'

        J = deque(temp)
        if not J:
            return False


if bfs():
    print(res)
else:
    print('IMPOSSIBLE')