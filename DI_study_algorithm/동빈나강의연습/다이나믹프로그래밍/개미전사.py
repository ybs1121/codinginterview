import sys

input = sys.stdin.readline

n = int(input())

warehouse = list(map(int, input().split()))
# odd = []
# even = []
# odd.append(warehouse[0])
#
# for i in range(1,n):
#     if i % 2 == 0:
#
#         odd.append(warehouse[i])
#     else:
#         even.append(warehouse[i])
#
# print(max(sum(odd),sum(even)))

d = [0] * 100

d[0] = warehouse[0]
d[1] = max(warehouse[0],warehouse[1])

for i in range(2,n):
    d[i] = max(d[i-1],d[i-2] + warehouse[i])


print(d[n-1])

