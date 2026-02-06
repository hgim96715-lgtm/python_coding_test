def solution(arr, queries):
    for q in queries:
        s,e,k=q
        for i,v in enumerate(range(s,e+1)):
            if v%k==0:
                arr[i]+=1
    return arr