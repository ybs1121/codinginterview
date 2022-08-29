import sys
input = sys.stdin.readline

n, m = map(int,input().split())
tree = list(map(int,input().split()))

start = 1
end = max(tree)

while start < end:
    tmp_sum = 0
    mid = (start + end) // 2

    for i in tree:
        cut = i - mid
        if cut > 0:
            tmp_sum += cut

    if tmp_sum >= m:
        start = mid + 1

    else:
        end = mid - 1

print(end)


