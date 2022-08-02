N = int(input()) # 사진틀 개수
Vote = int(input()) # 총 추천 회수
students = list(map(int, input().split())) # 추천 학생 번호
picture = []
score = []

for i in range(Vote):
    if students[i] in picture:
        for j in range(len(picture)):
            if students[i] == picture[j]:
                score[j] += 1
    else:
        if len(picture) >= N:
            for j in range(N):
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break
        picture.append(students[i])
        score.append(1)

picture.sort()
print(' '.join(map(str, picture)))