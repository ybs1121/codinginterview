# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    A.sort()
    if A[-1] <= 0:
        return 1
    A = set(A)
    A = list(A)
    max_idx = max(A)

    visited = [False] * (max_idx + 1)

    for i in A:
        if i > 0:
            visited[i-1] = True

    for i in range(len(visited)):
        if not visited[i]:
            return i+1

print(solution([2]))