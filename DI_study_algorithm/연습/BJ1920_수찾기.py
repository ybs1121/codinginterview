import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
a.sort()

m = int(input())
b = list(map(int,input().split()))


def b_search(st,ed,target):
    if st == ed:
        if a[st] == target:
            print(1)
            return 1
        else:
            print(0)
            return 0

    mid = (ed+st)//2

    if a[mid] < target:
        b_search(mid+1,ed,target)

    elif a[mid] > target:
        b_search(st,mid,target)

    else:
        print(1)
        return 1


for i in b:
   b_search(0,n-1,i)

print("-------------------------")

def bi_search(st,en,target):
    if st>en:
        return False

    mid=(st+en)//2

    if st==en:
        if a[st]==target:
            return 1

        else:
            return 0

    if a[mid]<target:
        bi_search(mid+1,en,target)
    else:
        bi_search(st,mid,target)




for i in b:
    print(bi_search(0,n-1,i))



