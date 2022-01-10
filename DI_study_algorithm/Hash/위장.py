from itertools import combinations
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 0
kind = []

for i,j in clothes:
    kind.append(j)

set_kind = set(kind)
count = []
for i in set_kind:
    count.append(kind.count(i))


for i in range(len(set_kind)):
    answer += len(list(combinations(kind,i+1)))


print(answer)

if len(set_kind) > 1:
    print("in")
    for i in count:
        if int(i) > 1:
            print("in",i)
            temp = []
            for j in range(i):
                temp.append(j)

            print(temp)

            for k in range(1,len(temp)):
                answer -= len(list(combinations(temp,k+1)))


print("anw%d"%answer)


#문제 풀이
def solution(clothes):
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        value = element[0]
        if key in closet:
            closet[key].append(value)
        else:
            closet[key] = [value]

    # ex) output: {'headgear': ['yellow_hat', 'green_turban'], 'eyewear': ['blue_sunglasses']}
    # 위와 같이 딕셔너리가 만들어진다.

    for key in closet.keys():
        result = result * (len(closet[key]) + 1)
    return result - 1
