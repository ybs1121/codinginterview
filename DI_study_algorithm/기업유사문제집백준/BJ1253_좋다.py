import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int,input().split()))

answer = 0
n_list.sort()
for i in range(n):
    start = 0
    end = n-2

    tmp_list = n_list[:i] + n_list[i+1:]
    while start < end:
        if tmp_list[start] + tmp_list[end] > n_list[i]:
            end -= 1
        elif tmp_list[start] + tmp_list[end] < n_list[i]:
            start += 1

        elif tmp_list[start] + tmp_list[end] == n_list[i]:
            answer += 1
            break



print(answer)