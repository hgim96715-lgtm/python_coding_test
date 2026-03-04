def solution(num_list):
    a=0
    b=0
    for v in num_list:
        if v%2:
            b+=1
        else:
            a+=1
    return [a,b]