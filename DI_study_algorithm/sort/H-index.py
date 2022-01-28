def solution(citations):
    citations.sort()
    for idx, citation in enumerate(citations):
        if citation >= len(citations) - idx:
            return len(citations) - idx
    return 0

if __name__ == "__main__":
    citations = [3, 0, 6, 1, 5]
    print(solution(citations))