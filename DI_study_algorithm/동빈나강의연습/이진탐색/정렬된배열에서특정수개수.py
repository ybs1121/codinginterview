import sys
from bisect import bisect_left,bisect_right
input = sys.stdin.readline

N,M = map(int,input().split())
array = list(map(int, input().split()))


left = bisect_left(array,M)
right = bisect_right(array,M)

print(right - left)