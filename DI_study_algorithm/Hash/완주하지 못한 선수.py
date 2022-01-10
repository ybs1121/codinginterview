# 내가 생각한 답안
def solution(participant, completion):
    answer = ''
    for i in completion:
        participant.remove(i)
    answer = participant[0]
    return answer

# 정확성은 다 통과, 효율성 실패.

#다른 사람 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]

if __name__ == "__main__":
    participant = ["mislav", "stanko", "mislav", "ana"]
    completion = ["stanko", "ana", "mislav"]
    print(solution(participant, completion))
