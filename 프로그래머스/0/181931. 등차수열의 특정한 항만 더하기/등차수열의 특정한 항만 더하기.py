def solution(a, d, included):
    arr=[a]
    answer = a
    result=0
    for i in range(len(included)-1):
        answer+=d
        arr.append(answer)
    for i,v in enumerate(arr):
        if included[i]==True:
            result+=v
    return result