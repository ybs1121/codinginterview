# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import sys


def solution(A):
    # write your code in Python 3.6
    answer = sys.maxsize

    tmp_a = A[0]
    tmp_b = sum(A[1:])
    answer = abs(tmp_a - tmp_b)

    for i in range(1, len(A) - 1):
        tmp_a += A[i]
        tmp_b -= A[i]
        answer = min(answer, abs(tmp_a - tmp_b))

    return answer

