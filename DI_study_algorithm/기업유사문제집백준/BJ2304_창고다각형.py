import sys
input = sys.stdin.readline

n = int(input())
stick = []

for i in range(n):
    temp = list(map(int,input().split()))
    stick.append(temp)
stick.sort()
print(stick)
start = stick[0][0]
end = stick[-1][0]
idx = -1
max_length = -1

for i in stick:
    if max_length < i[1]:
        max_length= i[1]
        idx = i[0]
print(max_length)
print(idx)

while True:
    for i in range(idx+1,end):
