# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    leafs = set()

    for i in range(len(A)):
        leafs.add(A[i])

        if len(leafs) == X:
            return i

    
    return -1



print(solution(5,[3]))


