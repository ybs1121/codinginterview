from itertools import permutations
def solution(expression):
    answer = []
    operators = ['+','-','*']
    operators = list(permutations(operators, 3))
    print(operators)

    separate = []
    tmp = ""
    for i in expression:
        if i == '-' or i == '+' or i == '*':
            tmp = int(tmp)
            separate.append(tmp)
            separate.append(i)
            tmp = ""
        else:
            tmp += i
    separate.append(int(tmp))

    for i in operators:
        tmp_separate = list(separate)
        for j in i:
            idx = 0
            while len(tmp_separate) != 1:
                k = tmp_separate[idx]
                if k == j:
                    if j == "-":
                        print("ll")
                        sum = tmp_separate[idx-1] - tmp_separate[idx+1]
                        del tmp_separate[idx + 1]
                        del tmp_separate[idx]
                        del tmp_separate[idx - 1]
                        tmp_separate.insert(idx - 1, sum)
                        idx = 0
                        continue

                    elif j == "+":

                        sum = tmp_separate[idx-1] + tmp_separate[idx+1]
                        del tmp_separate[idx+1]
                        del tmp_separate[idx]
                        del tmp_separate[idx-1]
                        tmp_separate.insert(idx - 1,sum)
                        idx = 0
                        continue

                    elif j == "*":
                        sum = tmp_separate[idx-1] * tmp_separate[idx+1]
                        del tmp_separate[idx + 1]
                        del tmp_separate[idx]
                        del tmp_separate[idx - 1]
                        tmp_separate.insert(idx - 1, sum)
                        idx = 0
                        continue
                idx += 1






    return answer

expression = "100-200*300-500+20"
print(solution(expression))