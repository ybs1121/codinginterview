def solution(n, k, cmd):
    answer = ''
    table = {}
    original_table = []
    recent_delete = []
    for i in range(n):
        table[i] = str(i)
        original_table.append(i)

    for c in cmd:
        print(k)


        if c[0] == "U":
            k -= int(c[2])

            # if k < 0:
            #     k = 0


        elif c[0] == "D":
            k += int(c[2])

            # if k+1 >len(table):
            #     k = len(table) -1


        elif c[0] == "C":
            tmp_key_list = list(table.keys())
            tmp_key = tmp_key_list[k] # 실제 가르키는 키
            recent_delete.append([tmp_key,table.pop(tmp_key)])

            if len(table) < k+1:
                k = 0



        elif c[0] == "Z":
            last_delete = recent_delete.pop()
            table[last_delete[0]] = last_delete[1]
            table = dict(sorted(table.items(), key=lambda x: x[0]))

            tmp_key_list = list(table.keys())
            tmp_key = tmp_key_list[k]

            if tmp_key < last_delete[0]:
                k += 1
                if k+1 > len(table):
                    k = 0









    key_list = list(table.keys())
    key_list.sort()

    key_list = set(key_list)
    original_table = set(original_table)
    delete_key = original_table - key_list

    print(delete_key)
    for i in range(n):
        answer+="O"

    answer = list(answer)

    for i in delete_key:
        answer[i] = "X"

    answer = "".join(answer)


    return answer


n = 8 # 표의 행 개수
k = 2 # 현재 포인터
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"] #커맨드
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n,k,cmd))

# OOXOXOOO
