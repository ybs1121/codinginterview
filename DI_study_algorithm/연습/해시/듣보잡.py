import sys

input = sys.stdin.readline

N , M = map(int,input().split())

name_list = []

for i in range(N + M):
    name_list.append(input())

no_listen = []
for i in range(N):
    no_listen.append(name_list[i])

no_see = []
for i in range(M):
    j = i + N
    no_see.append(name_list[j])
#
no_see_listen = []
for i in no_listen:
    if i in no_see:
        no_see_listen.append(i)

print(len(no_see_listen))
no_see_listen.sort()

for i in no_see_listen:
    print(i[:-2])