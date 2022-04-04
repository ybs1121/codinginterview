from itertools import *
def solution(dist):
    answer = []

    dist_max = 0
    point = []
    for i in range(len(dist)):
        point.append(i)

    for i in dist:
        tmp = max(i)
        if tmp > dist_max:
            dist_max = tmp

    printList = list(permutations(point, len(dist)))

    for i in printList:
        sum = 0
        i = list(i)
        for j in range(len(dist)-1):
            sum+=dist[i[j]][i[j+1]]
        if sum == dist_max:
            answer.append(i)




    return answer


dist = [[0,5,2,4,1],[5,0,3,9,6],[2,3,0,6,3],[4,9,6,0,3],[1,6,3,3,0]]
result = [[1,2,0,4,3],[3,4,0,2,1]]

print(solution(dist))