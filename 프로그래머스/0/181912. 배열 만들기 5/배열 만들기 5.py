def solution(intStrs, k, s, l):
    answer = []
    for str in intStrs:
        row=0
        row+=int(str[s:s+l])
        if row>k:
            answer.append(row)  
    return answer