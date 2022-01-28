def solution(array, commands):
    answer = []
    new_array = []
    for i in commands:
        for j in range(i[0]-1,i[1]):
            new_array.append(array[j])

        new_array = sorted(new_array)
        #print(new_array)

        answer.append(new_array[i[2]-1])
        new_array = []

    return answer

if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    print(solution(array,commands))
