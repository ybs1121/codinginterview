import heapq
def solution(operations):
    answer = []
    hp = []

    for i in operations:
        if i[0] == "I":
            heapq.heappush(hp, int(i[2:]))
        else:
            if i[2:] == "-1":
                if hp:
                    heapq.heappop(hp)
                else:
                    continue
            else:
                if hp:
                    hp = heapq.nlargest(len(hp), hp)[1:]
                    heapq.heapify(hp)
                else:
                    continue


    hp = sorted(hp)

    if len(hp) >= 1:
        # max = heapq.nlargest(len(hp), hp)[0]
        # heapq.heapify(hp)
        # answer.append(max)
        # answer.append(heapq.heappop(hp))
        answer.append(hp[-1])
        answer.append(hp[0])

    else:
        answer = [0, 0]
    return answer

if __name__ == "__main__":
    operations = ["I 7","I 5","I -5","D -1"]
    print(solution(operations))