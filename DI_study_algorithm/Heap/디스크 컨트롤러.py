import heapq


def solution(jobs):
    answer = 0

    before = -1
    after = 0
    count = 0
    task = []

    while count < len(jobs):
        for job in jobs:
            # 앞에 진행되고 있는 작업중에 작업 요청을 받았더라면 해당 task끝나기 전까지 사이의 시간 추가
            if before < job[0] <= after:
                answer += (after - job[0])
                # 중간에 작업 요청을 받았기 때문에 task에 추가시켜준다
                heapq.heappush(task, job[1])

        # task가 존재할때
        if task:
            # 다른 작업이 진행중이라 작업을 진행하지 못하지만 요청이 들어왔기 때문에 시간은 추가해준다
            answer += task[0] * len(task)

            # 시간 time변경
            before = after
            after += heapq.heappop(task)

            # 하나의 task가 끝났기 때문에 count를 추가시켜준다
            count += 1

        # task가 없을때
        else:
            # 시간만 흐르게 냅둔다
            after += 1

    return answer//len(jobs)

if __name__ == "__main__":
    jobs = [[1, 9],[0, 3], [2, 6]]
    print(solution(jobs))