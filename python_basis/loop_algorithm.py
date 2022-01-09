#문제 6071
n = 1
while n != 0:
    n = input()
    n = int(n)
    if n == 0:
        break
    print(n)

#문제 6072
n = input()
n = int(n)
while n != 0:
    print(n)
    n = n - 1

#문제 6074
c = ord(input())
a = ord('a')
while c >= a:
    print(chr(a),end= ' ')
    a = a + 1

#문제 6076
n = int(input())
for i in range(n+1):
    print(i)