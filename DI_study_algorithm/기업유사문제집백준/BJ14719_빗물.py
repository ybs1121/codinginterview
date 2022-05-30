import sys

input = sys.stdin.readline

h, w = map(int,input().split())
maps = list(map(int,input().split()))
max_h = maps[0]
rain = 0
stack = []

for i in range(1,w):
    if max_h > maps[i]:
        stack.append(maps[i])

    else:
        if stack:
            final_h = min(maps[i], max_h)
            while stack:
                tmp = stack.pop()
                rain += (final_h - tmp)

        max_h = maps[i]

if stack and maps[-1] != 0:
    final_h = min(maps[-1], max_h)
    while stack:
        tmp = stack.pop()
        rain += (final_h - tmp)






print(rain)


