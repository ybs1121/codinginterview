N, M  = input("입력 :").split(" ")
array = input().split(" ")
N = int(N)
M = int(M)

vistied = [[False] * M for i in range(N)]

# for i in range(M):
#     for j in range(N):
#         if array[i][j] == 1:
#             vistied[i][j] == True
# print(vistied)
steps = [(-1, 0) ,(1,0), (0,-1),(0,1)]
for i in range(M):
    tmp = []
    for j in range(N):
         if array[i][j] == 0:
             for step in steps:
                 if j + step[0] < 0 and j + step[0] > M - 1 and i + step[0] and i + step[0] > N -1:
                     array[i + step[0]]



from sys import stdin

N, M  = map(int,input("입력 :").split(" "))
matrix = [stdin.readline().rstrip() for _ in range(N)]

steps = [(1,0),(-1,0),(0,1),(0,-1)]

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
           for step in steps:
               if 0<= i + step[0] < N and 0<= j+step[1] < M:




