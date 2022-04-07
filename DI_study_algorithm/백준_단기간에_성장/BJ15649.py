N,M = map(int,input().split())

import itertools
kind = []
for i in range(N):
    kind.append(i+1)


answer = list(itertools.product(kind,repeat=M))

for i in answer:
    tmp = []
    check = 0
    for j in i:
        tmp.append(j)
    for k in range(1,len(tmp)):
        if tmp[k-1] > tmp[k]:
            check = 1
            break
    if check == 0:
        for z in tmp:
            print(z, end= " ")
        print()




