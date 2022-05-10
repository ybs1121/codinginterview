from collections import deque

def solution(board):
    answer = 0
    visited = [[False] * len(board) for _ in range(len(board))]
    cost_map = [[0] * len(board) for _ in range(len(board))]
    q = deque()
    q.append((0,0))


    nx = [1, 0, -1, 0]
    ny = [0, -1 ,0 ,1]
    conner_q = deque()
    count = 0

    idx = 0
    while q:


        idx += 1
        x,y = q.popleft()
        visited[x][y] = True
        conner_q.append((x,y))

        if len(conner_q) == 3:
            if conner_q[0][0] == conner_q[1][0] == conner_q[2][0]:
                print("Test")

        if x == len(board) - 1 and y == len(board) -1:
            print(cost_map[x][y])
            print(cost_map)


            print("end")
            break

        for i in range(4):
            next_x = x + nx[i]
            next_y = y + ny[i]


            if 0 <= next_x < len(board) and 0 <= next_y < len(board):
                if visited[next_x][next_y] == False and board[next_x][next_y] == 0:
                    q.append((next_x,next_y))
                    print("x = " + str(next_x) + " y = " + str(next_y))
                    cost_map[next_x][next_y] = cost_map[x][y] + 100








    return answer


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
board = [[0,0,0],[0,0,0],[0,0,0]]
print(solution(board))