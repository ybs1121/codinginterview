def dfs(n, computers, now, visited):
    visited[now] = True
    for connect in range(n):
        if connect != now and computers[now][connect] == 1:
            if visited[connect] == False:
                dfs(n,computers,connect, visited)

    return visited

def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            dfs(n, computers, com, visited)
            answer += 1
    return answer


