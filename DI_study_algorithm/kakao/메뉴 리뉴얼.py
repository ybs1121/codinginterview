def solution(orders, course):
    answer = []

    dict = {}

    for i in course:
        for j in orders:
            if len(j) == i:
                if not j in dict:
                    dict[j] = 0

    for i in dict.keys():
        key_len = len(i)

        for j in orders:
            count = 0
            for k in j:
                if k in i:
                    count += 1
            if count >= key_len:
                dict[i] += 1
    for k,v in dict.items():
        if v >= 2:
            answer.append(k)

    answer.sort()


    return answer



orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]

print(solution(orders,course))



