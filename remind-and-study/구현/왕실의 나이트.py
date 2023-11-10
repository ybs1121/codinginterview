data = input()

### 수직 두칸 수평 한칸
### 수평 두칸 수직 두칸
### 이동할 수 있는 경우는 결국 최대 8곳

print(ord(data[0]))

##열
x = int(data[1]) - 1
y = ord(data[0]) - 97

nx = [-2,-2,2,2,1,1,-1,-1]
ny = [1,-1,1,-1,-2,2,-1,1]
res = 0
for i in range(len(nx)):
    if 0<= x + nx[i] < 8 and 0 <= y + ny[i] < 8 :
        res += 1

print(res)
