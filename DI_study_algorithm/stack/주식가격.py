def solution(prices):
    answer = [0] * len(prices)

    size = len(prices)
    for i in range(len(prices)):
        for j in range(1, size):
            answer[i] += 1
            if prices[0] > prices[j]:
                break

        prices.pop(0)
        size = len(prices)


    return answer

if __name__ == "__main__":
    prices = [1, 2, 3, 2, 3]
    solution(prices)