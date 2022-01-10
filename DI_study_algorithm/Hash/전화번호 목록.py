# 내가 생각한 답안
def solution(phone_book):
    answer = True
    length = []
    for i in phone_book:
        length.append(len(i))

    min_length = min(length)
    min_index = length.index(min_length)

    j = 0
    for i in phone_book:
        if phone_book[j] == i:
            continue
        elif phone_book[j] in i[0:min_length]:
            answer = False
            break

    return answer
# 정확성: 62.5
# 효율성: 4.2
# 합계: 66.7 / 100.0

def solution(phone_book):
    answer = True
    head = phone_book[0][0:2]
    j = 0
    for i in phone_book:
        if j == 0:
            j = 1
            continue
        if head in i[0:2]:
            answer = False
            break;
    return answer
# 정확성: 58.3
# 효율성: 12.5
# 합계: 70.8 / 100.0

def solution(phone_book):
    answer = True
    head = []
    head2 = []
    for i in phone_book:
        head.append(i[0:2])
    for i in phone_book:
        head2.append(i[0:3])

    head_set = set(head)
    if len(head) != len(head_set):
        answer = False
    head_set2 = set(head2)
    if len(head2) != len(head_set2):
        answer = False
    return answer
