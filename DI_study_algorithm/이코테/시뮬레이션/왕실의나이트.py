import sys
input = sys.stdin.readline

point = input()
x = int(point[1])
y = ord(point[0]) - 96

nx = [-1,-1 , -2 , -2, 1, 1, 2, 2]
ny = [-2, 2 ,-1, 1, -2, 2, 1,-1, 1]
count = 0
for i in range(8):
    if 1 <= x + nx[i] <= 8 and 1 <= y + ny[i] <= 8:
        count += 1

print(count)