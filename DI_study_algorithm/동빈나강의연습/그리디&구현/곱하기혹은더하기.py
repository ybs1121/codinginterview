num = input()
num_list = list(num)

for i in range(len(num_list)):
    num_list[i] = int(num_list[i])


max = 0
for i in range(len(num_list)):
    if num_list[i] == 0 or max == 0:
        max += num_list[i]
    else:
        max*=num_list[i]


print(max)

##답안

data = input("답안")
result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num <= 1 or result <=1 :
        result += num
    else:
        result*num
print(result)
