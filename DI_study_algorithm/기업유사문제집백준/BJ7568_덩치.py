import sys

input = sys.stdin.readline

n = int(input())
people = []
for i in range(n):
    tmp = list(map(int,input().split()))
    people.append(tmp)

answer = []
for i in range(n):
    count = 1
    tmp_people = people[i]
    for j in range(n):
        tmp_people_j = people[j]

        if tmp_people_j[0] > tmp_people[0] and tmp_people_j[1] > tmp_people[1]:
            count += 1
    answer.append(count)

for i in answer:
    print(i,end = " ")




# import sys
# input = sys.stdin.readline
#
# n = int(input())
#
# people = []
# answer = []
# for i in range(n):
#     tmp = list(map(int,input().split()))
#     people.append(tmp)
#
# for i in people:
#     rank = 1
#     for j in people:
#         if j[0] > i[0] and j[1] > i[1]:
#             rank += 1
#     answer.append(rank)
#
#
#
# for i in answer:
#     print(i, end = " ")