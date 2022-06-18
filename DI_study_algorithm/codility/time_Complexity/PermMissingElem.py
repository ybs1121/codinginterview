# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    visited = [False] * (len(A) + 1)

    for i in A:
        visited[i - 1] = True


    for i in range(len(visited)):
        if not visited[i]:
            return i + 1



