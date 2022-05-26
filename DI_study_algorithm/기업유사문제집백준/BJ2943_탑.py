import sys

input = sys.stdin.readline

n = int(input())

tops = list(map(int,input().split()))
answer = []
# for i in range(n-1,-1,-1):
#     chk = False
#
#     for j in range(i-1,-1,-1):
#         if tops[j] >= tops[i]:
#             # print(tops[i])
#             # print(tops[j])
#             # print("-----------------")
#             answer.append(j+1)
#             chk = True
#             break
#
#     if chk == False:
#         answer.append(0)
#
# answer = answer[::-1]

# print(answer)


stack = [ [n-1,tops[-1]] ]
maps = [0] * n
for i in range(n-2,-1,-1):
    if stack[-1][1] > tops[i]:
        stack.append([i,tops[i]])
    else:
        while stack and stack[-1][1] < tops[i]:
            tmp = stack.pop()
            maps[tmp[0]] = i + 1
        stack.append([i,tops[i]])

for i in maps:
    print(i, end = " ")





