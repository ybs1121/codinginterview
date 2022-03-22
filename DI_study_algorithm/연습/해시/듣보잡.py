# import sys
#
# input = sys.stdin.readline
#
# N , M = map(int,input().split())
#
# no_listen = [input() for _  in range(N)]
#
# no_see = [input() for _  in range(M)]
#
# #
# no_see_listen = []
# for i in no_listen:
#     if i in no_see:
#         no_see_listen.append(i)
#
# print(len(no_see_listen))
# no_see_listen.sort()
#
# for i in no_see_listen:
#     print(i[:-2])


import sys

input = sys.stdin.readline

N , M = map(int,input().split())

all_list = [input() for _  in range(N+M)]

all_list.sort()

idx = 0

result = []

while idx < N+M-1 :
    if all_list[idx] == all_list[idx+1]:
        result.append(all_list[idx])
        idx += 2
    else:
        idx +=1

print(len(result))

for i in result:
    print(i[:-1])
