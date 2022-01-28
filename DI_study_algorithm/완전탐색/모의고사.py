def solution(answers):
    answer = []
    count = [0] * 3
    student1 = [1, 2, 3, 4, 5]
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    student1_pattern = 0
    student2_pattern = 0
    student3_pattern = 0

    for i in answers:



        if i == student1[student1_pattern]:

            count[0] += 1


        if i == student2[student2_pattern]:

            count[1] += 1


        if i == student3[student3_pattern]:

            count[2] += 1

        student1_pattern += 1
        student2_pattern += 1
        student3_pattern += 1


        if student1_pattern == 5:
            student1_pattern = 0
        if student2_pattern == 8:
            student2_pattern = 0
        if student3_pattern == 10:
            student3_pattern = 0

    answer.append(count.index(max(count)) + 1)

    for i in range(3):
        if i == count.index(max(count)):
            continue
        if count[i] == max(count):

            answer.append(i+1)

    sorted(answer)

    return answer
if __name__ == "__main__":
    answers = [1,3,2,4,2]
    print(solution(answers))
