def solution(score):
    arr=[]
    answer=[]
    for s in score:
        arr.append((s[0] + s[1]) / 2)
    arr_sort=sorted(arr,reverse=True)
    for v in arr:
        answer.append(arr_sort.index(v) + 1)
    return answer