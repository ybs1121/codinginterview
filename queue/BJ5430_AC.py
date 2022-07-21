import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for i in range(t):
    p = deque(input().rstrip())
    n = int(input())
    arrays = input().rstrip()
    check = False
    count = 0

    if len(arrays) > 2:
        arrays = list(map(int,arrays[1:-1].split(",")))
        q = deque(arrays)

    elif len(arrays) <= 2 and 'D' in p:
        q = deque()
        print("error")
        continue

    while p:
        c = p.popleft()

        if c == 'R':
            count += 1
        else:
            if q and count % 2 == 0:
                q.popleft()
            elif q and count % 2 == 1:
                q.pop()
            else:
                check = True
                break
    if check:
        print("error")
    else:
        if len(q) > 0:
            if count % 2 == 0:
                answer = str(list(q))

                answer = answer.replace(" ","")
                print(answer)
            else:
                q.reverse()
                answer = str(list(q))
                answer = answer.replace(" ","")
                print(answer)
        else:
            print("[]")







