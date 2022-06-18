# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):

    if len(A) == 0:
        return A

    for i in range(K):
        right = A.pop()
        A.insert(0, right)

    return A


