def solution(s):
    answer = 0
    str_answer = ""
    tmp_str = ""
    for i in s:
        if len(tmp_str) >= 3:
            if tmp_str == "zero":
                str_answer += "0"
                tmp_str = ""

            elif tmp_str == "one":
                str_answer += "1"
                tmp_str = ""

            elif tmp_str == "two":
                str_answer += "2"
                tmp_str = ""

            elif tmp_str == "three":
                str_answer += "3"
                tmp_str = ""

            elif tmp_str == "four":
                str_answer += "4"
                tmp_str = ""

            elif tmp_str == "five":
                str_answer += "5"
                tmp_str = ""

            elif tmp_str == "six":
                str_answer += "6"
                tmp_str = ""

            elif tmp_str == "seven":
                str_answer += "7"
                tmp_str = ""

            elif tmp_str == "eight":
                str_answer += "8"
                tmp_str = ""

            elif tmp_str == "nine":
                str_answer += "9"
                tmp_str = ""

        if 48 <= ord(i) <= 57:

            str_answer += i
        else:
            tmp_str += i


    if tmp_str != "":
        if tmp_str == "zero":
            str_answer += "0"
            tmp_str = ""

        elif tmp_str == "one":
            str_answer += "1"
            tmp_str = ""

        elif tmp_str == "two":
            str_answer += "2"
            tmp_str = ""

        elif tmp_str == "three":
            str_answer += "3"
            tmp_str = ""

        elif tmp_str == "four":
            str_answer += "4"
            tmp_str = ""

        elif tmp_str == "five":
            str_answer += "5"
            tmp_str = ""

        elif tmp_str == "six":
            str_answer += "6"
            tmp_str = ""

        elif tmp_str == "seven":
            str_answer += "7"
            tmp_str = ""

        elif tmp_str == "eight":
            str_answer += "8"
            tmp_str = ""

        elif tmp_str == "nine":
            str_answer += "9"
            tmp_str = ""


    answer = int(str_answer)
    return answer

print(solution("100"))
