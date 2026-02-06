def solution(l, r):
    answer = []
    for v in range(l, r + 1):
        va = ''
        isvalid = True            
        for a in str(v):
            if a in ('0', '5'):
                va += a
            else:
                isvalid = False
                break         
        if isvalid:
            answer.append(int(va))
    if answer==[]:
        answer.append(-1)
    return answer
