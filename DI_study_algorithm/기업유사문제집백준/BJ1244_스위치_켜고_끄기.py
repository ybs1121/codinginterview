import sys

input = sys.stdin.readline

switch_num = int(input())
switches = list(map(int, input().split()))
students = int(input())
switches = [-1] + switches

for i in range(students):
    s, idx = map(int,input().split())

    if s == 1:
        for j in range(idx,switch_num+1,idx):
            switches[j] = int(not switches[j])

    elif s == 2:
        switches[idx] = int(not switches[idx])

        left = idx - 1
        right = idx + 1

        while True:
            if left >= 1 and right <= switch_num:
                if switches[left] == switches[right]:
                    switches[left] = int(not switches[left])
                    switches[right] = int(not switches[right])
                    left -= 1
                    right += 1

                else:
                    break
            else:
                break

switches = switches[1:]
for i in range(0,switch_num,20):
    answer = ' '.join(str(s) for s in switches[i:i+20])
    print(answer)



