def solution(t, p):
    answer = 0
    for t1 in range(0,len(t)):
        res=t[t1:t1+len(p)]
        if len(res)==len(p) and res<=p:
            answer+=1
    return answer