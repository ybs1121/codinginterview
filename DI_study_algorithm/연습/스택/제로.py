import sys

input = sys.stdin.readline


K = int(input())
money = []
for i in range(K):
    call = int(input())

    if call == 0:
        money.pop()
    else:
        money.append(call)

print(sum(money))