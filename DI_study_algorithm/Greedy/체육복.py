def solution(n, lost, reserve):
    re_lo = set(lost) & set(reserve)

    answer = n - len(lost) + len(re_lo)

    lost = set(lost) - re_lo
    reserve = set(reserve) - re_lo

    lost = list(lost)
    reserve = list(reserve)




    for i in range(len(reserve)):
        for j in range(len(lost)):
            if abs(reserve[i]-lost[j]) == 1:
                answer += 1
                lost.pop(j)
                break

    return answer








if __name__ == "__main__":
    reserve = [1, 3, 5]
    lost = [2, 4]
    n = 5
    print(solution(n, lost, reserve))
