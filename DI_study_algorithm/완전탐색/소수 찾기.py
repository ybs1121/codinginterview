import itertools
def solution(numbers):
    answer = 0
    result = []
    number_list = []

    for i in range(0,len(numbers)):
        result.append(list(itertools.permutations(numbers, i+1)))

    #print(result)

    for i in result:
        for j in i:
            num = ""
            j = list(j)
            for k in j:
                num+=k

            number_list.append(int(num))

    number_list =set(number_list)
    number_list =list(number_list)


    for i in number_list:
        if i < 2:
            continue

        for j in range(2,i+1):


            if i%j == 0 and i !=j:

                break
            elif i%j == 0 and i ==j:
                answer+=1



    return answer


if __name__ == "__main__":
    answers = "011"
    print(solution(answers))
