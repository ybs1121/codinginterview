import sys

input = sys.stdin.readline

s = input().strip()
t = input().strip()

roots = [t]

for i in range(len(t)-len(s)):
    tmp = []

    for root in roots:
        if root[-1] == "A":
            tmp.append(root[:-1])

        if root[0] == "B":
            root = root[::-1]
            root = root[:-1]
            tmp.append(root)

    roots = tmp



if s in roots:
    print(1)
else:
    print(0)



