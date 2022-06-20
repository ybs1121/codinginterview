# import sys
# input = sys.stdin.readline
#
#
# answer = input().rstrip()
# m = int(input())
# cursor = len(answer)
#
# for i in range(m):
#     commend = input().rstrip()
#
#     if commend == 'L':
#         if cursor != -1:
#             cursor -= 1
#
#     elif commend == 'D':
#         str_len = len(answer)
#         if str_len > cursor:
#             cursor += 1
#
#     elif commend == 'B':
#         if -1 < cursor < len(answer):
#             answer = answer[:cursor] + answer[cursor+1:]
#             cursor -= 1
#         elif cursor == len(answer):
#             answer.pop()
#             cursor -= 1
#
#     else:
#         if cursor == -1:
#             answer = commend[2] + answer
#             cursor += 1
#         elif -1 < cursor < len(answer):
#             answer = answer[:cursor] + commend[2] + answer[cursor:]
#             cursor += 1
#         else:
#             answer = answer + commend[2]
#             cursor += 1
#     print("---------")
#     print(cursor)
#     print(answer)
#
#
#
#
# print(answer)


from sys import stdin

stk1 = list(stdin.readline().strip())
stk2 = []
n = int(input())
for line in stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + list(reversed(stk2))))

