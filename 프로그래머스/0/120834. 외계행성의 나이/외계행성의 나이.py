def solution(age):
    answer = ''
    for i in str(age):
        a=chr(97 + int(i))
        answer+=a
    return answer