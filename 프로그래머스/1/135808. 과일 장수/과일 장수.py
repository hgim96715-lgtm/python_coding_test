def solution(k, m, score):
    answer = 0
    u=[]
    score=sorted(score,reverse=True)
    for i in range(0, len(score), m):
        u=score[i:m+i]
        if len(u) == m:
            answer += u[-1] * m
    return answer