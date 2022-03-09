import sys

input = sys.stdin.readline

T = int(input())
vps = [list(map(str,input().rstrip())) for _ in range(T)]



for i in vps:
    left = []

    chk = 0

    for j in i:

        if j == '(':
            left.append(1)
        elif j == ')':
            if len(left) == 0:
                print("NO")

                chk = 1
                break
            else:
                left.pop()

    if chk == 0 and len(left) == 0:
        print("YES")
    elif chk == 1 and len(left) != 0:
        print("NO")









