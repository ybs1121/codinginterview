import sys

input = sys.stdin.readline

n = int(input())

tmp = [n] * 4

while n >= 1:

    if tmp[0]%5 == 0:
        tmp[0] = int(tmp[0]/5)

    if tmp[1] % 3 == 0:
        tmp[1] = int(tmp[1] / 3)

    if tmp[2] % 2 == 0:
        tmp[2] = int(tmp[2] / 2)

    tmp[3] = tmp[3] - 1



