def solution(x):
    sum_arr=sum(int(a) for a in str(x))
    return True if x%sum_arr==0 else False