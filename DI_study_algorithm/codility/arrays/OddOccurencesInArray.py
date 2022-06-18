# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6

    dict = {}

    for i in range(len(A)):
        if A[i] in dict:
            if dict[A[i]] == 1:
                del dict[A[i]]

        else:
            dict[A[i]] = 1

    for k, v in dict.items():
        if v == 1:
            return k