import sys
import copy
input = sys.stdin.readline

n, m  = map(int,input().split())

office = []
point_camera = []

for i in range(n):
    tmp = list(map(int,input().split()))
    office.append(tmp)

for i in range(n):
    for j in range(m):
        if 1 <= office[i][j] <= 5:
            point_camera.append((i,j,office[i][j]))

answer = sys.maxsize
count = 0

def check_watch(office_map, x, y, idx, count):
    global answer
    copy_office = copy.deepcopy(office_map)

    if idx == 1:
        for i in range(4):
            if i == 0:
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break

            elif i == 1:
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
            elif i == 2:

                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            elif i == 3:

                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            if count + 1 < len(point_camera):
                check_watch(office_map, point_camera[count + 1][0], point_camera[count + 1][1], point_camera[count + 1][2],
                            count + 1)
                office_map = copy.deepcopy(copy_office)
            else:
                c = 0
                for k in range(n):
                    for l in range(m):
                        if office_map[k][l] == 0:
                            c += 1
                answer = min(answer, c)
                office_map = copy.deepcopy(copy_office)

    elif idx == 2:
        for i in range(2):
            if i == 0:
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break

                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
            else:
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            if count + 1 < len(point_camera):
                check_watch(office_map, point_camera[count + 1][0], point_camera[count + 1][1], point_camera[count + 1][2],
                            count + 1)
                office_map = copy.deepcopy(copy_office)
            else:
                c = 0
                for k in range(n):
                    for l in range(m):
                        if office_map[k][l] == 0:
                            c += 1
                answer = min(answer, c)
                office_map = copy.deepcopy(copy_office)

    elif idx == 3:
        for i in range(4):
            if i == 0:
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            elif i == 1:
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                    for j in range(x + 1, n):
                        if office_map[j][y] == 0:
                            office_map[j][y] = '#'
                        elif office_map[j][y] == 6:
                            break
            elif i == 2:
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            elif i == 3:
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
            if count + 1 < len(point_camera):
                check_watch(office_map, point_camera[count + 1][0], point_camera[count + 1][1], point_camera[count + 1][2],
                            count + 1)
                office_map = copy.deepcopy(copy_office)
            else:

                c = 0
                for k in range(n):
                    for l in range(m):
                        if office_map[k][l] == 0:
                            c += 1
                answer = min(answer, c)
                office_map = copy.deepcopy(copy_office)

    elif idx == 4:
        for i in range(4):
            if i == 0:
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
            elif i == 1:
                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
            elif i == 2:
                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(y + 1, m):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break
            elif i == 3:
                for j in range(x + 1, n):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(x - 1, -1, -1):
                    if office_map[j][y] == 0:
                        office_map[j][y] = '#'
                    elif office_map[j][y] == 6:
                        break
                for j in range(y - 1, -1, -1):
                    if office_map[x][j] == 0:
                        office_map[x][j] = '#'
                    elif office_map[x][j] == 6:
                        break


            if count + 1 < len(point_camera):
                check_watch(office_map, point_camera[count + 1][0], point_camera[count + 1][1], point_camera[count + 1][2],
                            count + 1)
                office_map = copy.deepcopy(copy_office)
            else:
                c = 0
                for k in range(n):
                    for l in range(m):
                        if office_map[k][l] == 0:
                            c += 1
                answer = min(answer, c)
                office_map = copy.deepcopy(copy_office)
    elif idx == 5:
        for j in range(x - 1, -1, -1):
            if office_map[j][y] == 0:
                office_map[j][y] = '#'
            elif office_map[j][y] == 6:
                break

        for j in range(x + 1, n):
            if office_map[j][y] == 0:
                office_map[j][y] = '#'
            elif office_map[j][y] == 6:
                break
        for j in range(y - 1, -1, -1):
            if office_map[x][j] == 0:
                office_map[x][j] = '#'
            elif office_map[x][j] == 6:
                break
        for j in range(y + 1, m):
            if office_map[x][j] == 0:
                office_map[x][j] = '#'
            elif office_map[x][j] == 6:
                break

        if count + 1 < len(point_camera):
            check_watch(office_map,point_camera[count + 1][0],point_camera[count + 1][1],point_camera[count + 1][2], count + 1)
            office_map = copy.deepcopy(copy_office)
        else:
            c = 0
            for k in range(n):
                for l in range(m):
                    if office_map[k][l] == 0:
                        c += 1
            answer = min(answer, c)
            office_map = copy.deepcopy(copy_office)



if len(point_camera) > 0 :
    check_watch(office, point_camera[0][0], point_camera[0][1], point_camera[0][2], count)
else:
    c = 0
    for k in range(n):
        for l in range(m):
            if office[k][l] == 0:
                c += 1
    answer = min(answer, c)

print(answer)
