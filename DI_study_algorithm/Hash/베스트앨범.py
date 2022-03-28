def solution(genres, plays):
    rank = []
    dict = {}
    idx = 0
    for i,j in zip(genres,plays):
        if i in dict:
            dict[i].append([j,idx])
        else:
            dict[i] = [[j,idx]]
        idx += 1

    dict2 = {}
    for i in dict:
        sum = 0
        for j in dict[i]:
            sum+=j[0]
        dict2[i] = sum

    rank_list = []
    while dict2:
        tmp = max(dict2)
        rank_list.append(tmp)
        dict2.pop(tmp)




    for i in rank_list:
        dict[i].sort()
        print(dict)
        if len(dict[i]) == 1:

            tmp = dict[i].pop()
            rank.append(tmp[1])

        else:
            tmp_list = []
            for j in range(2):
                tmp = dict[i].pop()
                tmp_list.append(tmp)

            if tmp_list[0][0] == tmp_list[1][0]:
                if tmp_list[0][1] > tmp_list[1][1]:
                    rank.append(tmp_list[1][1])
                    rank.append(tmp_list[0][1])
                else:
                    rank.append(tmp_list[0][1])
                    rank.append(tmp_list[1][1])
            else:
                rank.append(tmp_list[0][1])
                rank.append(tmp_list[1][1])


    return rank





genres =["classic", "pop", "classic", "classic", "pop"]
plays =[500, 600, 150, 800, 2500]



print(solution(genres, plays))