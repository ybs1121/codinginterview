n = int(input())
three = "3"
h = 0
m = 0
s = 0
res = 0
three.find("1")
while h <= n:

    if three in str(h) or three in str(m) or three in str(s):
        print(h,m,s)
        res += 1

    s += 1

    if s == 60:
        s = 0
        m += 1

    if m == 60:
        m = 0
        h += 1

print(res)
