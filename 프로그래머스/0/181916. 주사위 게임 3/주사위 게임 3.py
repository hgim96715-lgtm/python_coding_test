def solution(a, b, c, d):
    arr=[a,b,c,d]
    answer = list(set(arr))
    if len(answer)==1:
        return 1111*answer[0]
    elif len(answer)==4:
        return min(answer)
    elif len(answer)==2:
        p,q=answer[0],answer[1]
        p_c, q_c = arr.count(p), arr.count(q)
        if p_c==3:
            return (10*p+q)**2
        elif q_c==3:
            return (10*q+p)**2
        else:
            return (p + q) * abs(p - q)
    elif len(answer)==3:
        one=[v for v in answer if arr.count(v)==1]
        # print(one)
        return one[0]*one[1]
    return answer