def solution(numlist, n):
    res=[]
    answer = {a: abs(n-a) for a in numlist}
    arr=sorted(answer.items(), key=lambda x: (x[1],-x[0]))
    for k,v in arr:
        res.append(k)
    return res