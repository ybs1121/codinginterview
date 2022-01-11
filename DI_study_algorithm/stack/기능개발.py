
def solution1(progresses, speeds):
    answer = []
    total = len(progresses)
    count = 0

    while len(progresses) > 0:
        for i in range(total):
            progresses[i]+= speeds[i]

        for i in range(total):
            if progresses[i] < 100:
                break

            count += 1

        if count > 0:
            for i in range(count):
                progresses.pop(i-1)
                answer.append(count)
                count = 0
                total = len(progresses)



    return answer


pro =[95, 90, 99, 99, 80, 99]
sp =[1, 1, 1, 1, 1, 1]


print(solution1(pro,sp))


def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0

    while len(progresses) > 0:
        if (progresses[0] + time * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1

        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
