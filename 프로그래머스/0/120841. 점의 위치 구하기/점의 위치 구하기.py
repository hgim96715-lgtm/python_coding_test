def solution(dot):
    a,b=dot
    if a*b>0 and (a<0 and b<0):
        return 3
    elif a*b>0 and (a>0 and b>0):
        return 1
    elif a*b<0 and (a<0 and b>0):
        return 2
    else:
        return 4