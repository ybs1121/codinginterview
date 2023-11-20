import sys

n, k = map(int, sys.stdin.readline().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort();
B = sorted(B, reverse=True);

print(A)
print(B)

for i in range(k):
    if A[i] < B[i]:
        A[i] = B[i]
    else:
        break

print(sum(A))