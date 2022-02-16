def solution(numbers, target):
    answer = 0
    roots = [0]

    for number in numbers:
        tmp = []
        for root in roots:
            tmp.append(root + number)
            tmp.append(root - number)
        roots = tmp


    for child in roots:
        if child == target:
            answer += 1
    print(roots)
    return answer
if __name__ == "__main__":
    target = 3
    numbers = [1, 1, 1, 1, 1]
    print(solution(numbers,target))