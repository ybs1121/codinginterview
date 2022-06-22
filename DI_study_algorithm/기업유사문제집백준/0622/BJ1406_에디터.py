import sys
input = sys.stdin.readline


stack1 = list(input().strip())

stack2 = []

m = int(input())

for i in range(m):
    commend = input().strip()
    if commend[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())

    elif commend[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())

    elif commend[0] == 'B':
        if stack1:
            stack1.pop()

    elif commend[0] == 'P':
        stack1.append(commend[2])


print(''.join(stack1 + list(reversed(stack2))))