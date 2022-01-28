def solution(progresses, speeds):
    answer = []
    total = len(progresses)
    min = 0
    count = 0
    while len(progresses) > 0:
        for i in range(total):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            for i in range(min, total):
                print(min)
                if progresses[i] >= 100:
                    count += 1
            answer.append(count)
            count = 0

    return answer

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