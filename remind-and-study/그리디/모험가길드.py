N = int(input())
m = list(map(int, input().split()))
m.sort()
res = 0
count = 0
#####아이디어#####
# 정렬
# 반복분 돌리면서 작은 수 별로 데리고 감

i = 0
for i in m:
    count += 1
    if count >= i:
        res += 1
        count = 0
print(res)