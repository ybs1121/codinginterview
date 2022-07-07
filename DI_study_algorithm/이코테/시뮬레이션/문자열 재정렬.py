import sys
input = sys.stdin.readline

s = input().rstrip()

strings = ""
number = 0

for i in s:
    if i.isalpha():
        strings += i
    else:
        number += int(i)

strings = sorted(strings)
if number > 0:
    strings = "".join(strings) + str(number)
else:
    strings = "".join(strings)

print(strings)
