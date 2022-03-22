import sys
input = sys.stdin.readline

N , K = map(int,input().split())

kind = []

for i in range(N):
    tmp = []
    w, v = map(int, input().split())
    tmp.append(w)
    tmp.append(v)
    kind.append(tmp)


from itertools import combinations

possibility =  []
for i in range(1,N+1):
    tmp = list(combinations(kind,i))
    possibility.append(tmp)

possibility_sum = []


for i in possibility:
    for j in i:
        result = 0
        check = 0
        for k in j:
            check += k[0]
            if check > K:
                break
            result+=k[1]
        if check <= K:
            possibility_sum.append(result)


print(max(possibility_sum))

def search(i,w):
    if i == N:
        return 0
    n1 = 0

    if(w + kind[i][0] <= K):
        n1 = kind[i][1] + search(i+1,w + kind[i][0])
    n2 = search(i+1,w)

    return max(n1,n2)

print(search(0,0))






