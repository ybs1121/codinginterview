import sys

input = sys.stdin.readline

N = int(input())
grahp = []
for i in range(N):
    grahp.append(list(map(int,input().rstrip())))

# print(N)
# print(grahp)
# print("-------------------------")

steps = [(1,0),(-1,0),(0,1),(0,-1)]


from collections import deque


sum = []
def bfs(x,y):
    if grahp[x][y] == 0:
        return False

    queue = deque()
    queue.append((x,y))
    apt = 0

    c = 0
    while queue:
        c += 1

        x,y = queue.popleft()
        for i in range(4):
            dx = x + steps[i][0]
            dy = y + steps[i][1]

            if 0 > dx or dx >= N or 0 > dy or dy >= N:
                continue

            elif grahp[dx][dy] == 0:

                continue


            elif grahp[dx][dy] == 1:
                grahp[dx][dy] = 0
                apt += 1
                queue.append((dx,dy))
    if c == 1:
        sum.append(1)
    else:
        sum.append(apt)
    return True




count = 0
for i in range(N):
    for j in range(N):
       if True == bfs(i,j):
           count += 1


print(count)
sum.sort()

for i in sum:
    print(i)