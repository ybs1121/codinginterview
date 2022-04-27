def solution(n, start, end, roads, traps):
    answer = 0
    edge = len(roads)
    INF = int(1e9)
    visited =[False] * (n + 1)
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    nodes = []
    for i in roads:
        graph[i[0]].append((i[1],i[2]))
    print(graph)

    def get_smellest_node():
        min_value = INF
        index = 0
        for i in range(n + 1):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                index = i
        return index

    def dijkstra(start,visited,graph):
        distance[start] = 0
        visited[start] = True

        for j in graph[start]:
            distance[j[0]] = j[1]


        for i in range(n - 1):
            now = get_smellest_node()
            visited[now] = True

            if now in traps:

                #visited =[False] * (n + 1)
                visited[now] = True
                #graph = [[] for i in range(n + 1)]

                for node in graph[now]:
                    a ,b = node
                    graph[now].remove((a,b))
                    graph[a].append((now,b))
                print(graph)


            for j in graph[now]:
                cost = distance[now] + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost


    dijkstra(start,visited,graph)

    answer = distance[end]


    print(distance[1:])

    return answer





n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2,3]

print(solution(n, start, end, roads, traps))