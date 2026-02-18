def solution(strArr):
    answer = []
    for v in strArr:
        if 'ad' in v:
            continue
        else:
            answer.append(v)
    return answer