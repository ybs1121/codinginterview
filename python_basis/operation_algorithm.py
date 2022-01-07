#문제 6032
n = input()
print(-n)

#문제 6033
n = ord(input())
print(chr(n+1))

#문제 6034
a = input()
b = input()
c = int(a) - int(b)
print(c)


#문제 6035
f1 = input()
f2 = input()
m = float(f1) * float(f2)
print(m)

#문제 6036
w,n = input().split(" ")
for i in range(int(n)):
    print(w)

#문제 6037
n = input()
w = input()

print(w * int(n))

#문제 6038
n1 = input()
n2 = input()

print(int(n1)**int(n2))

#문제 6039
n1 = input()
n2 = input()

print(int(n1)//int(n2))

#문제 6041
n1 = input()
n2 = input()

print(int(n1)%int(n2))

#문제 6044
n1 = input()
n2 = input()

print(int(n1)+int(n2))
print(int(n1)-int(n2))
print(int(n1)*int(n2))
print(int(n1)//int(n2))
print(int(n1)%int(n2))
print("%.2f"%(int(n1)/int(n2)))

#문제 6045
n1 , n2, n3 = input().split(" ")
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
sum = n1+n2+n3
print(sum, end=" ")
print("%.2f"%round(sum/3,2))
