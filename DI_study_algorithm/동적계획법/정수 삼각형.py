def solution1(triangle):
    answer = 0
    sum_list = [[triangle[0][0]]]
    max_len = len(triangle)
    if max_len == 1:
        return triangle[0][0]

    for i in range(1,len(triangle)):
        case_sum = []
        floor_lsit = sum_list[i - 1]
        idx = 1
        for j in floor_lsit:
            print(sum_list)
            #for k in range(0, 2):
            case_sum.append(j + triangle[i][idx-1])
            case_sum.append(j + triangle[i][idx])
            idx += 1
        print(idx)
            #idx -= 1 * i




        sum_list.append(case_sum)

    answer = max(sum_list[max_len-1])
    print(sum_list)

    return answer


def solution(triangle):
    answer = 0
    sum_list = [[triangle[0][0]]]
    max_len = len(triangle)
    if max_len == 1:
        return triangle[0][0]

    for i in range(1,len(triangle)):
        case_sum = []
        floor_list = sum_list[i - 1]
      #  print(floor_list)

        idx = 0
        for j in floor_list:
            for k in triangle[i][idx:idx+2]:
                case_sum.append(j + k)
            idx+=1



        sum_list.append(case_sum)

    answer = max(sum_list[max_len-1])

  #  print(sum_list)

    return answer


def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(i + 1):
            if j == 0:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j]
            elif i == j:
                triangle[i][j] = triangle[i][j] + triangle[i - 1][j - 1]
            else:
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j],
                                     triangle[i][j] + triangle[i - 1][j - 1])

    answer = max(triangle[-1])

    return answer


if __name__ == "__main__":
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    #triangle = [[1]]
    print(solution(triangle))
