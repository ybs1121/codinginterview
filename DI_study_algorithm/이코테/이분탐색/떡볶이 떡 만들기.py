import sys
input = sys.stdin.readline

n, m = map(int,input().split())

dduck = list(map(int,input().split()))

start = 0
end = max(dduck)
answer = 0

while start < end:
    mid = (start + end) // 2
    tmp_dduck = 0

    for i in dduck:
        d = i - mid
        if d > 0:
            tmp_dduck += d

    if tmp_dduck >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1



print(answer)

