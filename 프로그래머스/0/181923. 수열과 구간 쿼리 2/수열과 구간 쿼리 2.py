def solution(arr, queries):
    answer = []
    for q in queries:
        res=[]
        s,e,k=q
        c_arr=arr[s:e+1]
        for x in c_arr:
            if x>k:
                res.append(x)
        if res:
            answer.append(min(res))
        else:
            answer.append(-1)
    return answer