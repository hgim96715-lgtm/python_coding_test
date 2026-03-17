def solution(array, n):
    answer=0
    arr_str = [str(a) for a in array]
    for k in arr_str:
        if str(n)==k:
            answer+=1
    return answer