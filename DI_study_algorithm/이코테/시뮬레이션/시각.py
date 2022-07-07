import sys
input = sys.stdin.readline

n = int(input())
h = 0
m = 0
s = 0
count = 0
while h <= n:
    s += 1

    h = s//(60*60)
    rest_s = s % (60*60)
    m = rest_s//60
    time = str(h) + str(m) + str(rest_s%60)
    if '3' in time:
        count += 1


print(count)

h = int(input())

count = 0

for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)