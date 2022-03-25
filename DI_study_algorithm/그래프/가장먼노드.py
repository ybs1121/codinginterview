from collections import deque

def solution(n, edge):
    answer = 0
    edge.sort()

    graph = [[] for _ in range(n+1)]
    count = [0] * (n + 1)
    visited = [0] * (n + 1)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    queue = deque([[1,0]])
    while queue:
        tmp = queue.popleft()
        node = tmp[0]
        count_tmp = tmp[1]

        if visited[node] == 0:
            visited[node] = 1
            count[node] = count_tmp
            count_tmp += 1

            for i in graph[node]:
                queue.append([i,count_tmp])



    for i in count:
        if i == max(count):
            answer += 1

    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(n, edge))