# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    cnt = Y - X

    if cnt <= 0:
        return 0

    else:
        share = cnt // D
        rest = cnt % D

        if rest > 0:
            return share + 1

        else:
            return share



print(solution(1,11,2))