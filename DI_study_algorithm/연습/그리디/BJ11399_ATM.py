import sys

input = sys.stdin.readline

n = int(input())
people = list(map(int,input().split()))
people.sort()

answer = [0] * n
answer[0] = people[0]

count = 1

result =0
for i in range(len(people)+1):
    result += sum(people[0:i])

print(result)

