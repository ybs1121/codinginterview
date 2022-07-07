import sys
input = sys.stdin.readline



n = int(input())
steps = input().rstrip()

maps = [[0] * (n+1) for _ in range(n+1)]
x, y = 1, 1

for i in steps:
    if i == 'R':
        if 1 <= y + 1 <= n:
            y += 1
    elif i == 'L':
        if 1 <= y - 1 <= n:
            y -= 1
    if i == 'U':
        if 1 <= x - 1 <= n:
            x -= 1
    if i == 'D':
        if 1 <= x + 1 <= n:
            x += 1

print(str(x)+" " + str(y));
