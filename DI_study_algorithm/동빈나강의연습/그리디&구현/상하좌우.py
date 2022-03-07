import time

n = int(input())
command = input().split(" ")

print(command)

point = [1,1]

start = time.time()  # 시작 시간 저장

for i in command:
    if i == 'R':
        tmp = point[1] + 1
        if not tmp > n:
            point[1] = tmp
            print(point)

    elif i == 'L':
        tmp = point[1] - 1
        if not tmp < 1:
            point[1] = tmp
            print(point)

    elif i == 'U':
        tmp = point[0] - 1
        if not tmp < 1:
            point[0] = tmp
            print(point)

    elif i == 'D':
        tmp = point[0] + 1
        if not tmp > n:
            point[0] = tmp
            print(point)
print("------------------------")
print(point)
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간