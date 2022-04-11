import math


def is_prime_number(x):

    for i in range(2, int(math.sqrt(x)) + 1):

        if x % i == 0:
            return False
    return True

nums = []

while(True):
    n = int(input())
    if n == 0:
        break
    nums.append(n)


for n in nums:

    for i in range(3,n+1,2):
        num = n - i
        if num%2 == 1 and is_prime_number(num) and is_prime_number(i):
            print(str(n) + " = " + str(i) +" + " + str(num))
            break


