def solution(new_id):
    answer = ''
    new_id = new_id.lower()


    for i in new_id:
        if ord(i) < 97 or ord(i) > 122:
            if not 48 <= ord(i) <= 57:
                if i != '-' and i != '_' and i != '.':
                    new_id = new_id.replace(i ,'')

    for i in new_id:
        new_id = new_id.replace("..",".")

    if len(new_id) == 1 and new_id == '.':
        new_id = ""
    else:
        if new_id[0] == '.':
            new_id = new_id[1:]

    if new_id == "":
        new_id = ""
    else:
        if new_id[-1] == '.':
            new_id = new_id[0:-1]

    if new_id =="":
        new_id += 'a'

    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[0:-1]

    if len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id += new_id[-1]





    answer = new_id

    return answer

new_id = "...!@BaT#*..y.abcdefghijklm...."
new_id = "=.="

print(solution(new_id))