def solution(priorities, location):
    answer = 0

    max_prior = max(priorities)

    while True:
        temp = priorities.pop(0)

        if temp == max_prior:
            answer += 1
            if location == 0:
                break
            else:
                location-= 1
            max_prior = max(priorities)
        else:
            priorities.append(temp)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1




    return answer


if __name__ == "__main__":
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0

    print(solution(priorities,location))