def solution(s, n):
    answer = ''
    for s1 in s:
        if s1 == ' ':
            answer += ' '
        elif 'A' <= s1 <= 'Z':
            p = ord(s1) - ord('A')
            # print(p)
            new_p = (p + n) % 26
            # print(new_p)
            answer += chr(new_p + ord('A'))
        else:
            p=ord(s1)-ord('a')
            new_p=(p+n)%26
            answer+=chr(new_p+ord('a'))
    return answer