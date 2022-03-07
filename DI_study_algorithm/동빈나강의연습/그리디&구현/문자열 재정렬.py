str = input("입력값 :")

char_str = []
int_str = []

for i in str:
    if ord(i) >= 48 and ord(i) <= 57:
        int_str.append(i)
    else:
        char_str.append(i)

char_str.sort()

str = "".join(char_str)


int_list = map(int,int_str)
sum = sum(int_list)

print(str, end="")
print(sum)


