data = input()

alp = []
num = []

for i in data:
    if i.isalpha():
        alp.append(i)
    elif i.isdigit():
        num.append(i)
    else:
        ## 에러인 경우
        pass

alp.sort()

n = 0

for i in num:
    n += int(i)
result = ''.join(s for s in alp)
alp = str(alp)
print(result+str(n))