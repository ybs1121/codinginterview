

def isPalindrome(s: str):



    strs = []
    for char in s:
        if char.isalnum(): #isalnum() => 알파벳과 숫자인지 확인 함수
            strs.append(char)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

import re
def isPalindrome_2(s):

    s = s.lower()
    s = re.sub('[^a-z0-9]]','',s) # a-z, 0-9 외 다 제거

    return s==s[::-1] # 슬라이싱

if __name__ == '__main__':
    test_list = "atta"
    print(isPalindrome(test_list))
    print(isPalindrome_2(test_list))
