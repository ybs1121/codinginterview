import sys
input = sys.stdin.readline

S = list(input().rstrip())
bomb = list(input().rstrip())

stack = []

for i in range(len(S)):
    stack.append(S[i])
    if stack[-1] == bomb[-1] and len(stack) >= len(bomb):
        if stack[-len(bomb):] == bomb:
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")

#
# strings = strings.replace(explore,"")
#
#
# while True:
#     before = len(strings)
#     strings = strings.replace(explore, "")
#     after = len(strings)
#
#     if before == after:
#         break
#
# if len(strings) > 0:
#     print(strings)
# else:
#     print("FRULA")






#시간 초과
# while True:
#     if len(strings) < explore_len:
#         break
#
#     boom = False
#
#     for i in range(len(strings) - explore_len + 1):
#         if strings[i:i+explore_len] == explore:
#             boom = True
#             strings = strings[:i] + strings[i+explore_len:]
#             break
#
#     if not boom:
#         break
#
# if len(strings) > 0:
#     print(strings)
# else:
#     print("FRULA")




