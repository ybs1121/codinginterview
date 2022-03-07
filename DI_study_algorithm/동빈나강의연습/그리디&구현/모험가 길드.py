scared = input("공포도")
people = input("사람")

people_list = people.split(" ")

people_list.sort(reverse=True)

print(people_list)
result = 0

for i in people_list:
    group_num = int(i)

    people_list.pop(0)

    if group_num != 1:
        for j in range(group_num - 1):
            people_list.pop()

    result += 1

print(result)
# 리뷰 : 문제 이해를 잘못함

# 정답 핵심 코드

n = 5
data = list(map(int,input().split()))
data.sort()

for i in data:
    count += 1
    if count >= i:
        result +=1
        count = 0
print(count)