# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    b = format(N, 'b')

    b = str(b)
    answer = 0

    count = 0
    chk = 0

    for i in b:
        if i == '1':
            chk += 1

        if chk == 1 and i == '0':
            count += 1

        if chk == 2:
            chk -= 1
            answer = max(count, answer)
            count = 0

    return answer