from collections import deque
def bfs(x,y,visited,place):
    q = deque()
    q.append((x,y))
    people = []
    partition = []
    if place[x][y] == "P":
        people.append([x,y])
    if place[x][y] == "X":
        partition.append([x,y])

    visited[x][y] = True


    nx = [1,0,-1,0]
    ny = [0,1,0,-1]


    while q:
        x,y = q.popleft()
        for i in range(4):
            if 0 <= x + nx[i] < 5 and 0 <=  y + ny[i] < 5:
                if visited[x + nx[i]][y+ny[i]] == False:
                    q.append((x + nx[i],y + ny[i]))
                    visited[x + nx[i]][y+ny[i]] = True

                    # 거리두기 확인
                    if place[x + nx[i]][y + ny[i]] == "P":
                        for j in people:
                            manhattan_distance = abs(j[0]- (x + nx[i])) + abs(j[1]- (y + ny[i]))
                            count = 0
                            partition_count = 0
                            over_idx_count = 0
                            if manhattan_distance <= 2:
                                x = x + nx[i]
                                y = y + ny[i]

                                for k in range(4):
                                    if 0 <= x + nx[k] < 5 and 0 <= y + ny[k] < 5:
                                        if place[x + nx[k]][y + ny[k]] == "X":
                                            partition_count += 1
                                        if place[x + nx[k]][y + ny[k]] == "O":
                                            count += 1
                                    elif  0 > x + nx[k] or x + nx[k] >= 5 or 0 > y + ny[k] or y + ny[k] >= 5:
                                        print("상하좌우 없음")
                                        over_idx_count += 1
                                if over_idx_count+ partition_count != 4:
                                    print("들어오나요?")
                                    cross_x = [-1,-1,1,1]
                                    cross_y = [-1,1,1,-1]
                                    for k in range(4):
                                        if 0 <= x + cross_x[k] < 5 and 0 <= y + cross_y[k] < 5:
                                            if place[x + cross_x[k]][y + cross_y[k]] == "X":
                                                partition_count += 1
                                                print("대각선")
                                            if place[x + cross_x[k]][y + cross_y[k]] == "O":
                                                count += 1
                                            elif 0 > x + cross_x[k] or x + cross_x[k] >= 5 or 0 > y + cross_y[k] or y + cross_y[k] >= 5:
                                                print("대각선 없음")
                                                over_idx_count += 1

                                    if count+over_idx_count+partition_count != 8:
                                        print(count)
                                        return False




    return True



def solution(places):
    answer = []
    for i in range(5):
        visited = [[False] * 5 for _ in range (5)]
        chk = bfs(0,0,visited,places[i])
        if chk == True:
            answer.append(1)
        else:
            answer.append(0)

    print("__________")
    visited = [[False] * 5 for _ in range(5)]
    bfs(0,0,visited,places[4])

    return answer





places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
a = solution(places)

print(a)