import sys
from collections import Counter

input = sys.stdin.readline

s = input().strip()
s = s.upper()
l = Counter(s).most_common(2)

if len(l) == 1:
    print(l[0][0])
else:
    if l[0][1] > l[1][1]:
        print(l[0][0])
    else:
        print("?")

