import copy
import sys
input = sys.stdin.readline

n = int(input())
board = []

for i in range(n):
    board.append(list(map(int,input().split())))
answer = -1

# 최대 5번
def move(direction, grahp, count):
    # print(grahp)
    global answer

    # print(direction)
    # print("--")
    if count > 5:
        return
    maps = copy.deepcopy(grahp)

    #상
    if direction == 0:

        for col in range(n):
            row = n - 1
            while row >= 0:
                if maps[row][col] != 0 and maps[row][col] == maps[row - 1][col]:
                    maps[row][col] = 0
                    maps[row - 1][col] *= 2

                    for mv in range(row,n -1):
                        if maps[row][col] == 0:
                            maps[row][col],maps[row + 1][col] = maps[row + 1][col], maps[row][col]
                    row -= 2

                elif maps[row - 1][col] == 0 and maps[row][col] != 0:
                    maps[row - 1][col] = maps[row][col]
                    maps[row][col] = 0
                    row -= 1

                else:

                    row -= 1

        if answer <= max(map(max, maps)):
            answer = max(map(max, maps))
            for c in range(4):
                move(c,maps,count + 1)



    #하
    elif direction == 1:


        for col in range(n):
            row = 0
            while row < n - 1:
                if maps[row][col] != 0 and maps[row + 1][col] == maps[row][col]:
                    maps[row][col] = 0
                    maps[row + 1][col] *= 2

                    for mv in range(row, 0, -1):
                        if maps[row][col] == 0:
                            maps[row - 1][col], maps[row][col] = maps[row][col], maps[row - 1][col]
                    row += 2

                elif maps[row + 1][col] == 0 and maps[row][col] != 0:
                    maps[row + 1][col] = maps[row][col]
                    maps[row][col] = 0
                    row += 1
                else:
                    row += 1

        if answer <= max(map(max, maps)):
            answer = max(map(max, maps))
            for c in range(4):
                move(c,maps,count + 1)



    #좌
    elif direction == 2:
        print(grahp)

        for row in range(n):
            col = n - 1
            while col >= 0:
                if maps[row][col] != 0 and maps[row][col] == maps[row][col -1]:
                    maps[row][col] = 0
                    maps[row][col - 1] *= 2

                    for mv in range(col,n - 1):
                        if maps[col][row] == 0:
                            maps[row][col], maps[row][col + 1] = maps[row][col + 1],maps[row][col]

                    col -= 2
                elif maps[row][col - 1] == 0 and maps[row][col] != 0:
                    maps[row][col - 1] = maps[row][col]
                    maps[row][col] = 0
                    col -= 1

                else:
                    col -= 1


        if answer <= max(map(max, maps)):
            answer = max(map(max, maps))
            for c in range(4):
                move(c, maps, count + 1)

    #우
    elif direction == 3:

        for row in range(n):
            col = 0
            while col < n - 1:
                if maps[row][col] != 0 and maps[row][col + 1] == maps[row][col]:
                    maps[row][col] = 0
                    maps[row][col + 1] *= 2

                    for mv in range(col, 0, -1):
                        if maps[row][col] == 0:
                            maps[row][col],maps[row][col - 1] = maps[row][col - 1],maps[row][col]

                    col += 2

                elif maps[row][col + 1] == 0 and maps[row][col] != 0 :
                    maps[row][col + 1] = maps[row][col]
                    maps[row][col] = 0
                    col += 1
                else:
                    col += 1



        if answer <= max(map(max, maps)):
            answer = max(map(max, maps))
            for c in range(4):
                move(c, maps, count + 1)
#
# move(2,board,1)

copy_board = copy.deepcopy(board)
for i in range(4):
    move(i, board, 1)
    board = copy.deepcopy(copy_board)

print(answer)