from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

n, x = map(int,input().split())
arrays = list(map(int,input().split()))

left = bisect_left(arrays,2)
right = bisect_right(arrays,2)

print(right - left)