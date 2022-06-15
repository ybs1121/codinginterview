import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

robot_x, robot_y, robot_direction = map(int, input().split())

maps = []

for i in range(n):
    tmp = list(map(int, input().split()))
    maps.append(tmp)


def bfs(robot_x, robot_y, robot_direction):
    q = deque()
    q.append((robot_x, robot_y, robot_direction))
    chk = 0
    while q:
        print(q)
        x, y, direction = q.popleft()
        maps[x][y] = 2  # 청소

        if direction == 0:
            if 0 <= y - 1 < m and maps[x][y - 1] == 0:
                q.append((x, y - 1, 3))
                chk = 0
            else:
                chk += 1
                q.append((x, y, 3))


        elif direction == 1:
            if 0 <= x - 1 < n and maps[x - 1][y] == 0:
                q.append((x - 1, y, 0))
                chk = 0
            else:
                chk += 1
                q.append((x, y, 0))

        elif direction == 2:
            if 0 <= y + 1 < m and maps[x][y + 1] == 0:
                q.append((x, y + 1, 1))
                chk = 0

            else:
                chk += 1
                q.append((x, y, 1))

        elif direction == 3:
            if 0 <= x + 1 < n and maps[x + 1][y] == 0:
                q.append((x + 1, y, 2))
                chk = 0
            else:
                chk += 1
                q.append((x, y, 2))



        if chk == 4:
            print("in")
            if direction == 0:
                if x + 1 < n and maps[x + 1][y] != 1:
                    chk = 0
                    q.append((x + 1, y, direction))
                else:
                    break

            elif direction == 1:
                if y - 1 >= 0 and maps[x][y - 1] != 1:
                    chk = 0
                    q.append((x, y - 1, direction))
                else:
                    break

            elif direction == 2:
                if x - 1 >= 0 and maps[x - 1][y] != 1:
                    chk = 0
                    q.append((x - 1, y, direction))
                else:
                    break
            elif direction == 3:
                if y + 1 < m and maps[x][y + 1] != 1:
                    chk = 0
                    q.append((x, y + 1, direction))
                else:
                    break


bfs(robot_x, robot_y, robot_direction)

count = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 2:
            count += 1
for i in maps:
    print(i)

print(count)