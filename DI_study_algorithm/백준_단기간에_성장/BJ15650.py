N,M = map(int,input().split())

import itertools
kind = []
for i in range(N):
    kind.append(i+1)


answer = list(itertools.combinations(kind,M))

for i in answer:
    for j in i:
        print(j,end=" ")
    print()
