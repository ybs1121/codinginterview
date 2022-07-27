from collections import deque
import sys
input = sys.stdin.readline

r, c = map(int,input().split())

maps = []

for i in range(r):
    col = list(input().rstrip())
    maps.append(col)
water = []
for i in range(r):
    for j in range(c):
        if maps[i][j] == 'D':
            d = (i, j)
        if maps[i][j] == 'S':
            s = (i, j, 0)
        if maps[i][j] == '*':
            water.append((i, j))

nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]

water_q = deque()
water_q.append(water)
hedgehog_q = deque()
hedgehog_q.append(s)
chk = False

while water_q:
    waters = water_q.popleft()
    tmp_waters = set()
   # print(waters)
    for water_x, water_y in waters:
        for i in range(4):
            dx = water_x + nx[i]
            dy = water_y + ny[i]
            if 0 <= dx < r and 0 <= dy < c and maps[dx][dy] != 'D' and maps[dx][dy] != 'X':
                tmp_waters.add((dx,dy))
                maps[dx][dy] = '*'

    water_q.append(list(tmp_waters))

    if not hedgehog_q:
        break

    #print(hedgehog_q)
    for i in range(len(hedgehog_q)):
        hedgehog_x, hedgehog_y, count = hedgehog_q.popleft()

        for i in range(4):
            dx = hedgehog_x + nx[i]
            dy = hedgehog_y + ny[i]

            if dx == d[0] and dy == d[1]:
                chk = True
                answer = count + 1
                break

            if 0 <= dx < r and 0 <= dy < c and maps[dx][dy] == '.':
                hedgehog_q.append((dx, dy, count + 1))
                maps[dx][dy] = 'S'

    if chk:
        break
    # for i in maps:
    #     print(i)
    # print("------------------")

if chk:
    print(answer)
else:
    print("KAKTUS")

