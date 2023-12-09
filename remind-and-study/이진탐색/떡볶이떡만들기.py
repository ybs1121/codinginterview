import sys

n, k = map(int, sys.stdin.readline().split())

data = list(map(int, input().split()))

print(n, k)
print(data)

start = 1
end = 2000000000
result = -1

while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in data:
        cut = i - mid
        if cut > 0:
            sum += cut
    if sum < k:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)