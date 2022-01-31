def solution(brown, yellow):
    answer = [0] * 2
    sum = brown + yellow
    for i in range(3,sum//2):
        j = sum/i
        if j % 1 == 0:
            if 2*j + 2*i == brown + 4:
                answer[0] = int(j)
                answer[1] = int(i)




    answer.sort(reverse=True)
    return answer


def solution2(brown, yellow):
    answer = [0] * 2
    sum = brown + yellow
    min = 9999999
    for i in range(3, sum // 2):
        div = sum / i

        if div % 1 == 0:

            if min > abs(i - int(sum / i)):
                answer[0] = i
                answer[1] = int(sum / i)
        min = abs(answer[0] - answer[1])

    answer.sort(reverse=True)
    return answer


if __name__ == "__main__":
    brown = 10
    yellow = 2
    print(solution(brown,yellow))
