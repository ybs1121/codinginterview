# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()

    for i in range(len(A)):
        if i + 1 != A[i]:
            return 0

    return 1
