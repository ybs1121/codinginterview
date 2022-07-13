import sys
input = sys.stdin.readline

k, n = map(int,input().split())

lan_lines = []
for i in range(k):
    lan_lines.append(int(input()))


start = 1
end = max(lan_lines)
answer = 0
while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in lan_lines:
        count += (i // mid)

    if count >= n:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)