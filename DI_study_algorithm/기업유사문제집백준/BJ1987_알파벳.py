import sys
input = sys.stdin.readline

r,c = map(int,input().split())
maps = []
for i in range(r):
    tmp = list(input().rstrip())
    maps.append(tmp)
print(maps)

chk = set()
answer = 0
nx = [1, 0, -1, 0]
ny = [0, 1, 0, -1]
def dfs(x,y,c):
    global answer
    answer = max(answer, c)

    for i in range(4):
        xx = x + nx[i]
        yy = y + ny[i]
        if 0 <= xx < r and 0 <= yy < c and not maps[xx][yy] in chk:
            chk.add(maps[xx][yy])
            dfs(xx, yy, c+1)
            chk.remove(maps[xx][yy])

chk.add(maps[0][0])
dfs(0,0,1)

print("---------")

print(answer)




r, c = map(int, input().split())
maps = []
for _ in range(r):
    maps.append(list(input().rstrip()))
print(maps)
ans = 0
alphas = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    global ans
    ans = max(ans, count)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not maps[nx][ny] in alphas:
            alphas.add(maps[nx][ny])
            dfs(nx, ny, count+1)
            alphas.remove(maps[nx][ny])
alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)


