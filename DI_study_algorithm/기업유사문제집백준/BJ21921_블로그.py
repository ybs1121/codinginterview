import sys
input = sys.stdin.readline

x,n = map(int,input().split())
visited = list(map(int,input().split()))

max_day = x - n
sum_list = [0] * x
sum_list[0] = visited[0]

for i in range(1,n):
    sum_list[i] = sum_list[i-1] + visited[i]

for i in range(n,x):
    sum_list[i] = sum_list[i-1] + visited[i] - visited[i-n]



#
# for i in range(max_day):
#     sum_list.append(sum(visited[i:i+n])) # 지속해서 합을 구해야 하기 떄문에 시간 초과


num_max = max(sum_list)
if num_max == 0:
    print("SAD")
else:

    print(num_max)

    count = 0
    for i in sum_list:
        if i == num_max:
            count += 1
    print(count)
