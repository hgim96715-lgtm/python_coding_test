def solution(myString):
    answer = ''
    for v in myString:
        if v=='a' or v=='A':
            answer+=v.upper()
        else:
            answer+=v.lower()
    return answer