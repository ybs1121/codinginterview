import sys
input = sys.stdin.readline
answer = []
for i in range(4):
    result = list(map(int,input().split()))

    split_teams = []

    for j in range(0,16,3):
        split_teams.append([result[j],result[j+1],result[j+2]])

    
    print("-----")
print(answer)