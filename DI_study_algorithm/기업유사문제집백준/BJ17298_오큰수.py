import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

stack = []

maps = [-1] * n
for i in range(n):
    if not stack:
        stack.append([i,a[i]])

    while stack and stack[-1][1] < a[i]:
        tmp = stack.pop()
        maps[tmp[0]] = a[i]
    stack.append([i,a[i]])

for i in maps:
    print(i, end = " ")




