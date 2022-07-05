import sys
input = sys.stdin.readline

n = int(input())
schedule = {}
min_start = sys.maxsize
max_start = -1

for i in range(n):
    start, end = map(int,(input().split()))
    min_start = min(start,min_start)
    max_start = max(start,max_start)

    if start in schedule:
        diff = end - start
        org_diff = schedule[start][1]

        if diff < org_diff:
            schedule[start] = diff
    else:
        schedule[start] = (end, end - start)
if n == 1:
    print(1)
else:
    answer = -1
    for i in range(min_start,max_start + 1):
        count = 1
        if i in schedule:
            next_time = schedule[i][0]
            while next_time <= max_start:
                if next_time in schedule:
                    if schedule[next_time][0] == next_time:
                        next_time = schedule[next_time][0] + 1
                    else:
                        next_time = schedule[next_time][0]
                    count += 1
                else:
                    next_time += 1


        answer = max(answer,count)



    print(answer)
