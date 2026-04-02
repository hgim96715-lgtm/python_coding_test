def solution(x):
    arr = list(str(x))
    sum_arr=sum(int(a) for a in arr)
    return True if x%sum_arr==0 else False