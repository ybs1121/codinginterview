N = int(input())

classes = list(map(int,input().split()))

overseer = list(map(int,input().split()))


people = 0

for i in classes:
    tmp = i - overseer[0]
    if tmp <= 0:
        people += 1
        continue

    sub_overseer = tmp // overseer[1]
    if sub_overseer == 0:
        people += 2

    else:
        if tmp % overseer[1] > 0:
            people += sub_overseer + 2
        else:
            people += sub_overseer + 1

print(people)