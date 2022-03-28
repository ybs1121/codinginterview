import sys
input = sys.stdin.readline

x = int(input())
stairway = []

for i in range(x):
    tmp = int(input())
    stairway.append(tmp)


score = [0] * x

if x == 1:
    score[0] = stairway[0]
elif x==2:
    score[1] = score[0] + stairway[1]
else:
    score[0] = stairway[0]
    score[1] = score[0] + stairway[1]
    score[2] = max(stairway[1] + stairway[2], score[0] + stairway[2])

    for i in range(3,x):
        score[i] = max(score[i-3] + stairway[i - 1] + stairway[i], score[i-2]+stairway[i])

print(score[-1])
