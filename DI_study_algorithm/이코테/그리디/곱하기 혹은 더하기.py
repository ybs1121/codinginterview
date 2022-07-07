import sys
input = sys.stdin.readline

numbers = input().rstrip()

numbers = numbers.replace('0','')

answer = 1

for i in numbers:
    answer *= int(i)

print(answer)


numbers = input().rstrip()
result = int(numbers[0])

for i in range(1,len(numbers)):
    num = int(numbers[i])

    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)