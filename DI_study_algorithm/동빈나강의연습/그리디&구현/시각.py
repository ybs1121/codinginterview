N = input()
h = 0
m = 0
s = 0
count = 0
while h <= int(N):
    time = str(h) + str(m) + str(s)
    if '3' in time:
        count += 1
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1

print(count)