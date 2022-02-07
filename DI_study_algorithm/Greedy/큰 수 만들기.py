import itertools

def solution(number, k):
    answer = ''
    index = []
    result = []
    number_list = list(number)
    for i in range(len(number)):
        index.append(i)

    result.append(list(itertools.permutations(index, k)))

    test = result[0]


    items = list(set([tuple(set(item)) for item in test]))




    answer_int = []

    for i in items:
        k = 0

        for j in i:

            number_list.pop(j - k)
            k+= 1
        answer_int.append(int(''.join(number_list)))

        number_list = list(number)





    #print(number_list)




    return str(max(answer_int))




def solution(number, k):
    # stack에 입력값을 순서대로 삽입
    stack = [number[0]]
    for num in number[1:]:
        # 들어오는 값이 stack 값보다 크면, 기존의 값을 제거하고 새로운 값으로 바꿈
        # 참고 : len(stack) > 0 == stack
        while len(stack) > 0 and stack[-1] < num and k > 0:
            # 값을 한개 빼서 k는 1이 제거
            k -= 1
            # 내부의 값을 제거
            stack.pop()
        # 새로운 값을 삽입
        stack.append(num)
    # 만일 충분히 제거하지 못했으면 남은 부분은 단순하게 삭제
    # 이렇게 해도 되는 이유는 이미 큰 수부터 앞에서 채워넣었기 때문
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)



    return answer






print(solution("1924",2))
print(answer("1924",2))