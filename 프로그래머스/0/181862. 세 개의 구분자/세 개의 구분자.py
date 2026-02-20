def solution(myStr):
    answer = []
    str=""
    for s in myStr:
        if s in "abc":
            if str:
                answer.append(str)
                str=""
        else:
            str+=s
    if str:
        answer.append(str)
    return answer if answer else ["EMPTY"]