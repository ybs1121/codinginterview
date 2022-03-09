import sys

input = sys.stdin.readline

N , M = map(int,input().split())
A = [1,2,5,4,3] #list(map(int, input().split()))
B = [5,5,6,6,7]


A.sort()
B.sort(reverse= True)

for i in range(M):
    A[i] = B[i]

print(sum(A))