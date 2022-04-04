import sys
input = sys.stdin.readline

line = int(input())

answer = []

for i in range(line):
    tmp = input()
    answer.append(tmp[:-1])


for i in answer:
    sum = 0
    plus = 1
    for j in i:
        if j == 'O':
            sum += plus
            plus += 1
        else:
            plus = 1
    print(sum)