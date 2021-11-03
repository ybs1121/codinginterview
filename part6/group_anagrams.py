import collections


def groupAnangrams(s):
    anagrams = collections.defaultdict(list)

    for word in s:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


if __name__ == "__main__":

    test = ["eat","tea","tan", "ate" , "nat", "bat"]

    print(groupAnangrams(test))

    a = 'cba'
    b = ['c','b','a']
    print(sorted(a)) # 문자열, 리스트를 정렬하여 리스트로 리턴
    b.sort() # r = b.sort() 하면 None값 리턴, 리스트에서만 사용
    print(b)