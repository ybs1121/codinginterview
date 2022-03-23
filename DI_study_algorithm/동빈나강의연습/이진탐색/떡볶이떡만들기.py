import sys
input = sys.stdin.readline

N,M = map(int,input().split())
rice_cake = list(map(int, input().split()))

rice_cake.sort()
height = []
def search(target,start,end,count):
    if start > end:
        return None

    mid = (start+end)//2
    sum = 0
    for i in range(count):
        if rice_cake[i] > mid:
            sum += (rice_cake[i] - mid)

    if sum >= target:
        height.append(mid)
        search(target, mid + 1, end, count)
    elif sum < target:
        search(target, start, mid-1, count)



search(M,0,rice_cake[-1],N)

print(max(height))