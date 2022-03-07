def solution(tickets):
    answer = []
    root = []
    count = 0
    for i in tickets:
        tmp = []
        tmp.append(0)
        tmp.append(i)
        root.append(tmp)


    root[0][0] = 1

    tmp = root[0]

    test = []
    test.append(root[0][1][0])

    for ticket in tickets:
        count = 0

        for i in range(1,len(root)):
            if root[i][0] == 0 and tmp[1][1] == root[i][1][0]:
                if count == 0:
                    root[i][0] = 1
                    test.append(tmp[1][1])
                    tmp = root[i]
                    count += 1




    test.append(tmp[-1][1])


    print(test)





    return answer


# def dfs(tickets, x , k, chk):
#     next = tickets[x][1]
#     print(chk)
#     for i in range(len(tickets)):
#         if k == i:
#             pass
#         elif chk[i] == False and tickets[k] == tickets[i]:
#             chk[i] = True
#             print(tickets)
#             dfs(tickets, x , k, chk)

def dfs(start,tickets,chk,root):

    for i in range(len(tickets)):
        if start == tickets[i][0] and chk[i] == False:
            start = tickets[i]
            chk[i] = True
            root.append(start[0])
            dfs(start,tickets,chk,root)



def solution1(tickets):
    answer = []
    INC = []

    idx = 0
    for i in tickets:
        if i[0] =='ICN':
            INC.append(idx)
        idx += 1


    chk = [False] * len(tickets)

    root = []

    for k in INC:
        tmp = []
        for i in range(len(tickets)):
            chk[k] = True
            dfs(tickets[k][1],tickets,chk,tmp)
            chk = [False] * len(tickets)
        root.append(tmp)

    print(root)



    # for k in INC:
    #
    #     chk[k] = True
    #     for i in range(len(tickets)):
    #         if k == i:
    #             pass
    #         elif chk[i] == False and tickets[k] != tickets[i]:
    #             chk[i] = True
    #             dfs(tickets,i,k,chk)
    #     chk = [False] * len(tickets)



    return answer



from collections import defaultdict

def solution2(tickets):
    answer = []
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    print(routes)


    for key in routes.keys():
        routes[key].sort(reverse=True)
    print(routes)



    stack = ['ICN']

    stack = ['ICN']
    while stack:
        tmp = stack[-1]

        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())

        print(stack)
        print(routes)

    answer.reverse()

    return answer


if __name__ == "__main__":
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

    print(solution2(tickets))