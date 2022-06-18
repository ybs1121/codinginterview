def solution(N, A):
    answer = [0]*N
    max_counter = N+1
    cache = 0
    maximum = 0

    for num in A:
        if num < max_counter:
            if answer[num-1] < cache:
                answer[num-1] = cache + 1
            else:
                answer[num-1] += 1

            if answer[num-1] > maximum:
                maximum = answer[num-1]
        else:
            cache = maximum

    for idx in range(N):
        if answer[idx] < cache:
            answer[idx] = cache

    return answer