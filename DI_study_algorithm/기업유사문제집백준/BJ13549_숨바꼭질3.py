import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int,input().split())
answer = 0



if n == k:
    print(0)
elif n > k:
    print(n-k)

else:
    maps = [sys.maxsize] * 100001
    q = deque()
    q.append((n,0))

    while q:
        value,time = q.popleft()

        if (value + 1) < 100001 and maps[value + 1] > time + 1:
            q.append((value + 1, time + 1))
            maps[value + 1] = time + 1

        if 1 <= (value - 1) < 100001 and maps[value - 1] > time + 1:
            q.append((value - 1, time + 1))
            maps[value - 1] = time + 1

        if (value * 2) < 100001 and maps[value*2] > time:
            q.append((value * 2, time))
            maps[value*2] = time
    print(maps[k])



#
# times = [[n,0]]
# answer = 0
#
#
# maps = [sys.maxsize] * 100001
# q = deque()
# q.append((n,0))
# if n == k:
#     print(0)
# elif n > k:
#     print(n-k)
#
# else:
#     while q:
#         value,time = q.popleft()
#
#         if (value + 1) < 100001 and maps[value + 1] > time + 1:
#             q.append((value+1,time+1))
#             maps[value + 1] = time + 1
#
#         if 1 <= (value - 1) < 100001 and maps[value - 1] > time + 1:
#             q.append((value - 1,time+1))
#
#             maps[value - 1] = time + 1
#
#         if value * 2 < 100001 and maps[value * 2] > time:
#             q.append((value*2,time))
#             maps[value*2] = time
#
#     print(maps[k])