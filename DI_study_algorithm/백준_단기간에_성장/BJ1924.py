import sys
input = sys.stdin.readline

x,y = map(int,input().split())
sum_day = 0

for i in range(1,x):
    if i in [1,3,5,7,8,10,12]:
        sum_day += 31
    elif i in [4,6,9,11]:
        sum_day += 30
    elif i == 2:
        sum_day += 28

sum_day += y
day = sum_day%7
if day == 1:
    print("MON")
if day == 2:
    print("TUE")
if day == 3:
    print("WED")
if day == 4:
    print("THU")
if day == 5:
    print("FRI")
if day == 6:
    print("SAT")
if day == 0:
    print("SUN")
