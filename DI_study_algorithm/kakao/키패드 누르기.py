import math


def solution(numbers, hand):
    answer = ''
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left = '*'
    right = '#'
    left_now = [3,0]
    right_now = [3,2]

    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            left = i
        if i == 3 or i == 6 or i == 9:
            answer += 'R'
            right = i
        if i == 2 or i == 5 or i == 8 or i == 0:
            for k in range(4):
                for j in range(3):
                    if phone[k][j] == i:
                        now = [k,j]
                    if phone[k][j] == left:
                        left_now = [k,j]
                    if phone[k][j] == right:
                        right_now = [k,j]

            distance_left = abs(now[0] - left_now[0]) + abs(now[1] - left_now[1])
            distance_right =abs(now[0] - right_now[0]) + abs(now[1] - right_now[1])

            if distance_right > distance_left:
                answer += 'L'
                left = i
            elif distance_right < distance_left:
                answer += 'R'
                right = i
            elif distance_right == distance_left:
                if hand == 'right':
                    answer+='R'
                    right = i
                else:
                    answer +='L'
                    left = i
            # print(i)
            # print(right)
            # print(left)
            # print(distance_right)
            # print(distance_left)



    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers,hand))