n = 25
m = 5
result = 0
while True:
    if n == 1:
        break

    if n % m == 0 :
        result += 1
        n = n / m
    else:
        n -= 1


print(result)
