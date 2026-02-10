def solution(my_strings, parts):
    answer = ''
    for i,v in enumerate(my_strings):
        p,q=parts[i]
        answer+=v[p:q+1]
    return answer