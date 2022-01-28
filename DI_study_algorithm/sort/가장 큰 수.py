import itertools


def solution(numbers):
    result = list(itertools.permutations(numbers, len(numbers)))
    # print(result)
    change_list = []
    for i in result:
        str_change = ''
        for j in i:
            str_change += str(j)
        change_list.append(str_change)

    for i in range(len(change_list)):
        change_list[i] = int(change_list[i])

    answer = max(change_list)
    answer = str(answer)
    return answer

# 대부분의 문제는 시간 초과

if __name__ == "__main__":
    numbers = [6, 10, 2]
    print(solution(numbers))
