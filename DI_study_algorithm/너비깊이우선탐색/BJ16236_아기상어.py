from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

maps = []
answer = 0

for _ in range(n):
    maps.append(list(map(int,input().split())))


fishes = []


for i in range(n):
    for j in range(n):
        if maps[i][j] == 9:
            shark = (i,j,answer)
        elif 1 <= maps[i][j] <= 6:
            fishes.append((i,j,maps[i][j]))

#상어가 먹을 수 있는 물고기가 없을때 종료



if len(fishes) == 0 or (len(fishes) == 1 and fishes[0][-1] >= 2):
    print("조건 1")
    answer = 0

elif len(fishes) == 1:
    print("조건2")
    q = deque()
    q.append(shark)
    visited = [[False] * n for _ in range(n)]

    while q:
        x, y, sec = q.popleft()

        visited[x][y] = True

        if x == fishes[0][0] and y == fishes[0][1]:
            answer = sec

        nx = [1, 0, -1, 0]
        ny = [0, 1, 0, -1]

        for i in range(4):
            zx = x + nx[i]
            zy = y + ny[i]
            if 0 <= zx < n and 0 <= zy < n and not visited[zx][zy]:
                q.append((zx, zy, sec + 1))

else:
    #가장 가까운 먹을 수 있는 물고기를 찾는다.
    print("조건3")

    most_close_fishes = set()
    shark_size = 2
    eat_fish = 0

    while fishes:
        for i in range(len(fishes)):
            q = deque()
            q.append(shark)
            visited = [[False] * n for _ in range(n)]

            while q:
                x, y, sec = q.popleft()
                visited[x][y] = True
                if x == fishes[i][0] and y == fishes[i][1] and shark_size > fishes[i][2]:
                    most_close_fishes.add((x,y,sec,i))
                    break

                    #좌표,값,인덱스
                nx = [1, 0, -1, 0]
                ny = [0, 1, 0, -1]

                for i in range(4):
                    zx = x + nx[i]
                    zy = y + ny[i]

                    if 0 <= zx < n and 0 <= zy < n and not visited[zx][zy]:
                        q.append((zx, zy, sec + 1))

        if len(most_close_fishes) >= 1:
            most_close_fishes = list(most_close_fishes)
            most_close_fishes = sorted(most_close_fishes, key = lambda x: (x[2], x[0], x[1]))
          #  print(most_close_fishes)
            answer += most_close_fishes[0][2]
            del fishes[most_close_fishes[0][3]]
            maps[most_close_fishes[0][0]][most_close_fishes[0][1]] = 0

            eat_fish += 1
            if eat_fish == shark_size:
                eat_fish = 0
                shark_size += 1

            shark = (most_close_fishes[0][0], most_close_fishes[0][1],0)
            most_close_fishes = set()

        else:
            print(most_close_fishes)
            break

print(answer)