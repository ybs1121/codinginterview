def solution(s):
    answer = 0

    for i in range(len(s)):
        stack = []
        chk = True

        for j in range(len(s)):
            if (j == 0 and s[j] == '}') or (j == 0 and s[j] == ']') or (j == 0 and s[j] == ')'):
                chk = False
                break

            if s[j] == '{' or s[j] == '[' or s[j] == '(':
                stack.append(s[j])
            else:
                if not stack:
                    chk = False
                    break
                elif stack[-1] == '{' and s[j] == '}':
                    stack.pop()
                elif stack[-1] == '[' and s[j] == ']':
                    stack.pop()
                elif stack[-1] == '(' and s[j] == ')':
                    stack.pop()
                else:
                    chk = False
                    break
        if chk and not stack:
            answer += 1

        s = s[1:] + s[0]




    return answer



s = "[]{}()"
print(solution(s))