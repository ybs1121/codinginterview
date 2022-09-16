import sys

input = sys.stdin.readline

t = int(input())


def dfs(node):
    global end
    if visited[node]:
        end = node

        return
    visited[node] = True
    chk_group.append(node)

    dfs(dic[node])




for i in range(t):
    n = int(input())
    choices = list(map(int, input().split()))
    re_choices = [0]
    re_choices.extend(choices)
    dic = {}

    for j in range(1, len(re_choices)):
        dic[j] = re_choices[j]



    # 깊이 탐색 - > 시작과 끝이 같은지 확인하면 된다.
    answer = []

    visited = [False] * (n + 1)
    for k in range(1, n + 1):

        start = k
        end = -1
        chk_group = []
        dfs(start)
        # print("-----")

        if start != end:
            for l in chk_group:
                visited[l] = False
            pass
        else:
            answer.extend(chk_group)

    print(n - len(set(answer)))
