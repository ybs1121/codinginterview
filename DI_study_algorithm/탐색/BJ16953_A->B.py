from collections import deque
import sys
input = sys.stdin.readline

a,b = map(int,input().split())

q = deque()
q.append((a,1))

answer = []

while q:
    idx, count = q.popleft()
    double = idx * 2
    side_plus = idx * 10 + 1

    if double < b:
        q.append((double,count + 1))

    if side_plus < b:
        q.append((side_plus,count + 1))

    if double == b:
        answer.append(count + 1)
    if side_plus == b:
        answer.append(count + 1)


if answer:
    print(min(answer))
else:
    print(-1)

