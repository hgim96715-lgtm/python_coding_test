def solution(array):
    arr= [str(a) for a in array]
    str_arr=''.join(arr)
    answer=str_arr.count('7')
    return answer