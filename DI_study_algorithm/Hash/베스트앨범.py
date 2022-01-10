genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


temp = [[0 for col in range(2)] for row in range(len(plays))]
total = {}
for i in range(len(plays)):
    temp[i][0] = genres[i]
    temp[i][1] = plays[i]

print(temp)

for i in temp:
    key = i[0]
    value = i[1]
    if key in total:
        total[key].append(value)
    else:
        total[key] = [value]
sum = {}
for i in total.keys():
    a = total[i]
    sum_temp = 0
    for j in range(len(a)):
        sum_temp += a[j]
    sum[i] = sum_temp
print(sum)

sdict= sorted(sum.items(), reverse=True)
rank = []
for i in sdict:
    t = total[i[0]]
    t.sort(reverse=True)
    print(t)
    for j in t:
        rank.append(plays.index(j))

print(rank)


