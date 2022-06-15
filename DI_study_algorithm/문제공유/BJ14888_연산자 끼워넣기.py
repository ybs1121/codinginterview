import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
operators = list(map(int,input().split()))

max_answer = -sys.maxsize
min_answer = sys.maxsize

def dfs(depth,total,plus,minus,multiply,divide):
    global max_answer, min_answer

    if depth == n:
        max_answer = max(total,max_answer)
        min_answer = min(total,min_answer)
        return


    if plus:
        dfs(depth + 1, total + a[depth], plus - 1, minus, multiply, divide)

    if minus:
        dfs(depth + 1, total - a[depth], plus, minus - 1, multiply, divide)

    if multiply:
        dfs(depth + 1, total * a[depth], plus, minus, multiply -1, divide)

    if divide:
        dfs(depth + 1, int(total / a[depth]), plus, minus, multiply, divide -1)


dfs(1,a[0],operators[0],operators[1],operators[2],operators[3])

print(max_answer)
print(min_answer)

