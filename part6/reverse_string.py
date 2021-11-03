def my_reverse_string(s): # 내가 생각한 답
    return s[::-1]

def reverse_string(s):
    s.reverse() # reverse 는 리스트만


if __name__ == '__main__':
    test = 'hello'
    test2 =['h','e','l','l','o']
    print(my_reverse_string(test2))
    reverse_string(test2)
    print(test2)
