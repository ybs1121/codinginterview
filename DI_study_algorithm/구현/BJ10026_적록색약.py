from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
pic = []
for i in range(n):
    pic.append(list(input().rstrip()))

color_blindness = [[False] * n for _ in range(n)]
not_color_blindness = [[False] * n for _ in range(n)]

answer_blindness = 0
answer_not_blindness = 0

nx = [1, 0,-1, 0]
ny = [0, 1, 0, -1]

def not_color_blindness_dfs(x, y,visited):

    if visited[x][y]:
        return False
    visited[x][y] = True

    for i in range(4):
        zx = x + nx[i]
        zy = y + ny[i]

        if 0 <= zx < n and 0 <= zy < n and not visited[zx][zy] and pic[x][y] == pic[zx][zy]:
            not_color_blindness_dfs(zx,zy,visited)

    return True

def color_blindness_dfs(x, y,visited):

    if visited[x][y]:
        return False

    visited[x][y] = True

    for i in range(4):
        zx = x + nx[i]
        zy = y + ny[i]

        if pic[x][y] == 'R' or pic[x][y] == 'G':
            if 0 <= zx < n and 0 <= zy < n and not visited[zx][zy] and (pic[zx][zy] == 'R' or pic[zx][zy] == 'G'):
                color_blindness_dfs(zx,zy,visited)

        else:
            if 0 <= zx < n and 0 <= zy < n and not visited[zx][zy] and pic[x][y] == pic[zx][zy]:
                color_blindness_dfs(zx,zy,visited)

    return True



for i in range(n):
    for j in range(n):
        chk1 = not_color_blindness_dfs(i,j,not_color_blindness)
        chk2 = color_blindness_dfs(i,j,color_blindness)
        if chk1:
            answer_not_blindness += 1
        if chk2:
            answer_blindness += 1

print(answer_not_blindness, end = " ")
print(answer_blindness)


