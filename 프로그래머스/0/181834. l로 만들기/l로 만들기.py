def solution(myString):
    answer = ''
    for v in myString:
        if ord(v)<ord('l'):
            answer+='l'
        else:
            answer+=v
    return answer