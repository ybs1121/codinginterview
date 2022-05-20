import sys
input = sys.stdin.readline

n,m = map(int,input().split())

memo = []

for i in range(n):
    memo.append(input().strip())

for i in range(m):
    key_word = list(input().strip().split(","))
    for j in key_word:
        if j in memo:
            memo.remove(j)
    print(len(memo))