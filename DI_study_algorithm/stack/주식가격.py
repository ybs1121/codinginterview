import time
def solution(prices):
    answer = [0] * len(prices)
    start_time = time.perf_counter()
    size = len(prices)

    for i in range(len(prices)):
        for j in range(1, size):
            answer[i] += 1
            if prices[0] > prices[j]:
                break

        prices.pop()
        size = len(prices)

    time_duration = time.perf_counter() - start_time
    print(time_duration)
    return answer

from collections import deque

def solution1(prices):
    queue = deque(prices)
    answer = []
    start_time = time.perf_counter()
    while queue:
        price = queue.popleft()
        sec = 0
        for q in queue:
            sec += 1
            if price > q:
                break
        answer.append(sec)
    time_duration = time.perf_counter() - start_time
    print(time_duration)
    return answer
if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3, 2]
    solution(prices)


