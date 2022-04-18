n = int(input())
nums = list(map(int,input().split()))
operator = list(map(int,input().split()))

answer = [nums[0]] * (4)
nums.pop(0)


def backtracking(operator,nums):
    if sum(operator) == 0:
        return

    for num in nums:
        tmp = []
        for i in range(1):

            nums.pop(0)
            if operator[0] > 0:
                answer[0] += num
                operator[0] -= 1
                tmp.append(answer[0])
                backtracking(operator,nums)
                operator[0] += 1

            if operator[1] > 0:
                answer[1] -= num
                operator[1] -= 1
                tmp.append(answer[1])
                backtracking(operator, nums)
                operator[1] += 1

            if operator[2] > 0:
                answer[2] *= num
                operator[2] -= 1
                tmp.append(answer[2])
                backtracking(operator, nums)
                operator[2] += 1

            if operator[3] > 0:
                answer[3] = answer[3]// num
                operator[3] -= 1
                tmp.append(answer[3])
                backtracking(operator, nums)
                operator[3] += 1

backtracking(operator,nums)
print(answer)


import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)


