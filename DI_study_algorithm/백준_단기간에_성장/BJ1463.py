import sys
input = sys.stdin.readline

x = int(input())
count = 0
while x > 1:
    check = 0

    if x%3 == 0:
        x = int(x/3)
        check = 3
        count += 1


    if x % 2 == 0:
        if check == 0 and (x-1)%3 != 0:
            x = int(x / 2)
            check = 2
            count += 1




    if check == 0:
        x = x - 1
        count += 1



print(count)