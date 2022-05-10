def solution(s):
    answer = 0
    max_len = len(s)
    counter = []
    count_s = []

    for i in range(1,len(s)//2+1):
        c = 1
        tmp_s = ""
        for j in range(1,len(s),i):
            if s[j-i:j] == s[j:j+i]:
                c += 1
            else:
                if c != 1:
                    tmp_s += str(c) + s[j-i:j]
                    c = 1

                else:
                    tmp_s += s[j-i:j]



        if c != 1:
            tmp_s += str(c) + s[j-i:j]
        else:
            tmp_s += s[j:j+i]

        counter.append(len(tmp_s))
        count_s.append(tmp_s)




    #print(min(counter))
    print(count_s)
    return answer


s = "aabbaccc"

print(solution(s))