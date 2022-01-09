#문제 6065
a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
if a%2 == 0:
    print(a)
if b%2 ==0:
    print(b)
if c%2 ==0:
    print(c)

#문제 6067
a = input()
a = int (a)

if a<0:
    if a%2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")

#문제 6068
a = input()
a = int (a)

if a>=90:
    print('A')
elif a>=70:
    print('B')
elif a>=40:
    print('C')
else:
    print('D')

#문제 6069:
c = input()
if c =='A':
    print("best!!!")
elif c == 'B':
    print("good!!")
elif c == 'C':
    print("run!")
elif c == 'D':
    print("slowly~")
else:
    print("what?")
#문제 6070
m = input()
m = int(m)
if m>=3 and m<=5:
    print("spring")
elif m>=6 and m<=8:
    print("summer")
elif m>=9 and m<=11:
    print("fall")
else:
    print("winter")




