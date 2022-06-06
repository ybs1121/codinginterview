import sys
input = sys.stdin.readline

n = int(input())

people = []
answer = []
for i in range(n):
    tmp = list(map(int,input().split()))
    people.append(tmp)

for i in people:
    rank = 1
    for j in people:
        if j[0] > i[0] and j[1] > i[1]:
            rank += 1
    answer.append(rank)



for i in answer:
    print(i, end = " ")