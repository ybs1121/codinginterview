import heapq
import sys
input = sys.stdin.readline

n,m = map(int,input().split())

words = []
for i in range(n):
    words.append(input().strip())

dict = {}

for i in words:
    if len(i) >= m:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
#dict = sorted(dict.items(), key=lambda x: x[1],reverse= True)

sort_list = []

for k,v in dict.items():
    sort_list.append((v,len(k),k))

sort_list = sorted(sort_list,key = lambda x :(-x[0],-x[1],x[2]))

for i in sort_list:
    print(i[2])