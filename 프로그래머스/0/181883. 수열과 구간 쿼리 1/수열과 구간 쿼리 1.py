def solution(arr, queries):
    for q in queries:
        s,e=q
        # print(s,e)
        for i in range(s,e+1):
            arr[i]+=1
    return arr