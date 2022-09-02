import sys
input = sys.stdin.readline

x, y = map(int,input().split())

answer = -1

origin_score = y * 100 // x

start = 1
end = 1000000000

while start <= end:
    mid = (start + end) // 2

    tmp_x = x + mid
    tmp_y = y + mid

    tmp_answer = (tmp_y * 100) // tmp_x
    if origin_score < tmp_answer:
        end = mid - 1
        answer = mid

    elif origin_score >= origin_score:
        start = mid + 1



print(answer)
