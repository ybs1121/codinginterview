#문제 6063
a, b = input().split(" ")
a = int(a)
b = int(b)
c = (a if(a>=b) else b)
print(c)

#문제 6064
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
d = min(a,b,c)
print(d)