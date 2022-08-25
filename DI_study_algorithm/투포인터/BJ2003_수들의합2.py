import sys
input = sys.stdin.readline

n, m = map(int,input().split())
maps = list(map(int,input().split()))

answer = 0


maps_sum = 0
end = 0

for start in range(n):

    while maps_sum < m and end < n:
        maps_sum += maps[end]
        end += 1

    if maps_sum == m:
        answer += 1

    maps_sum -= maps[start]

print(answer)





