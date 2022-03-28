import sys
input = sys.stdin.readline

t = int(input())
test_case = []
for i in range(t):
    test_case.append(int(input()))
result = [0] * 11

max = max(test_case)

result[1] = 1
result[2] = 2
result[3] = 4
count = 0
for i in range(4,max+1):

    sum = 0

    for j in range(i-3,i):
        sum += result[j]

    result[i] = sum

for i in test_case:
    print(result[i])
