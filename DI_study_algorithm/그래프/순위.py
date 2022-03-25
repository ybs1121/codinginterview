from collections import deque

def solution(n, results):
    answer = 0
    graph = [[] for _ in range(n+1)]


    for i in results:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    connect = []


    for i in range(len(graph)):
        if len(graph[i]) == n - 1:
            connect.append(i)
            answer += 1



    connect = deque([connect[0]])

    visited = [0] * (n+1)

    while connect:
        tmp = connect.popleft()

        if visited[tmp] == 0:
            visited[tmp] = 1
            for i in results:

                if i[0] == tmp:
                    connect.append(i[0])
                    answer += 1


    return answer


n = 5
results = [[1, 3], [1, 2], [1, 2], [1, 2], [2, 5]]
print(solution(n, results))