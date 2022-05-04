from collections import deque
def solution(gems):
    answer = [1,len(gems)]
    kind_gems = list(set(gems))
    temp = ["nothing"]
    gems = temp + gems

    for start in range(1,len(gems) - len(kind_gems)):
        temp_kind_gems = list(kind_gems)
        temp_gems = list(gems)
        end = start
        if answer[1] - answer[0] == len(kind_gems):
            break

        while end < len(temp_gems):
            if temp_gems[end] in temp_kind_gems:
                temp_kind_gems.remove(temp_gems[end])

            if not temp_kind_gems:
                break
            end += 1


        if not temp_kind_gems:
            if answer[1] - answer[0] > end - start:
                answer[0] = start
                answer[1] = end
            if answer[1] - answer[0] == end - start:
                if answer[0] > start:
                    answer[0] = start
                    answer[1] = end




    return answer

gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
#gems = 	["AA", "AB", "AC", "AA", "AC"]
#gems = ["XYZ", "XYZ", "XYZ"]
gems = ["DIA", "EM", "EM", "RUB", "DIA"]
print(solution(gems))