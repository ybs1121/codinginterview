import sys
input = sys.stdin.readline

n = int(input())
request = list(map(int,input().split()))
government = int(input())

start = 0
end = max(request)

target = government
answer = [0,0,0]

while start <= end:
    divide = (start + end) // 2
    sum = 0
    for i in request:
        if divide > i:
            sum += i
        else:
            sum += divide

    if sum == target:
         answer[0] = divide
         break

    elif sum < target:
        start = divide + 1
        answer[1] = divide
    else:
        end = divide - 1
        answer[2] = divide

max_answer = -1
for i in answer:
    need_money = 0
    for j in request:
        if i >= j:
            need_money += j
        else:
            need_money += i

    if government - need_money >= 0 and max_answer < i:
        max_answer = i

print(max_answer)