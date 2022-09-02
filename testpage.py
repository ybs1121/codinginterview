import collections
def solution(s):
    sH=collections.Counter(s)
    print(sH)
    for index, val in enumerate(s):
        if sH[val]==1:
            return index+1
    return -1


print(solution("softbananas"))#2
print(solution("stringshowtime"))#3
print(solution("showshowmine"))#9
print(solution("statitsics"))#3
print(solution("aabb"))#8
