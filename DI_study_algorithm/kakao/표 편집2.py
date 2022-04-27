def solution(n, k, cmd):
    answer = ''
    table = []
    orignal_table = []
    for i in range(n):
        table.append([i,str(i)])
        orignal_table.append(i)


#    orignal_table = list(table)

    delete_list = []


    for i in cmd:
        action = i[0]


        if action == 'U':
        #    print("U action")
            k -= int(i[2])

        elif action == 'D':
         #   print("D action")
            k += int(i[2])

        elif action == 'C':
          #  print("C action")
            delete_list.append(table.pop(k))
            table_len = len(table)
            if k == table_len:
                k -= 1


        elif action == 'Z':
           # print("Z action")
            recent_delete = delete_list.pop()
            table.append(recent_delete)
            table.sort()
            idx = 0
            for i in table:
                if recent_delete[0] == i[0]:
                    break
                idx += 1

            if k >= idx:
                k += 1

    recent_table = []
    for i in table:
        recent_table.append(i[0])

    delete = set(orignal_table) - set(recent_table)
    delete = list(delete)
    answer = ['O'] * n

    for i in delete:
        answer[i] = 'X'

    # print(delete)

    answer = "".join(answer)



    return answer






n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))

print(1e9)