def solution(id_list, report, k):
    answer = [0] * len(id_list)
    can_report = {}
    report_user_count = {}
    mail_count = {}
    for i in id_list:
        can_report[i] = list(id_list)
        report_user_count[i] = 0
        mail_count[i] = []



    for i in report:
        user, report_user = i.split(" ")
        if report_user in can_report[user]:
            report_user_count[report_user] += 1
            temp = can_report[user]
            temp.remove(report_user)
            can_report[user] = temp
            #print(can_report)
            mail_count[user].append(report_user)


    idx = 0
    for i in mail_count:

        for j in mail_count[i]:
            if report_user_count[j] >= k:
                answer[idx] += 1
        idx += 1













    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))