import sys
input = sys.stdin.readline

N = int(input())

result = 0
for i in range(10**N):
    if i < 10:
        result += 1
    else:
        check = True
        for j in range(N-1,-1,-1):
            if j == N-1:
              number = i//(10**j)
              rest_number = i%(10**j)
            else:
                if number <= rest_number//(10**j):
                    number = rest_number//(10**j)
                    rest_number = i%(10**j)
                else:
                    check = False
                    break

        if check == True:
            result += 1



print(result%10007)


