import sys
input = sys.stdin.readline

n, k = map(int,input().split())
c = 0
while n > 1:
    if n % k == 0:
        n = n//k
        c += 1
    else:
        n -= 1
        c += 1
print(c)


n, k = map(int,input().split())
result = 0
while True:
    target = (n // k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    result += 1
    n //= k

result += (n - 1)
print(result)
