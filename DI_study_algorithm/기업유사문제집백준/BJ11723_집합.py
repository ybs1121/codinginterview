import sys
input = sys.stdin.readline
x = int(sys.stdin.readline().rstrip())
commends = []
s = []


# for i in range(x):
#     tmp = list(input().split())
#     commends.append(tmp)

def add(x):
    if x not in s:
        s.append(x)


def remove(x):
    if x in s:
        s.remove(x)


def check(x):
    if x in s:
        print(1)
    else:
        print(0)


def toggle(x):
    if x in s:
        s.remove(x)
    else:
        s.append(x)


def all():
    s = [x for x in range(1, 21)]


def empty():
    s = []


for i in range(x):
    commend = list(sys.stdin.readline().split())
    if commend[0] == "add":
        add(commend[1])
    elif commend[0] == "remove":
        remove(commend[1])
    elif commend[0] == "check":
        check(commend[1])
    elif commend[0] == "toggle":
        toggle(commend[1])
    elif commend[0] == "all":
        all()
    elif commend[0] == "empty":
        empty()
