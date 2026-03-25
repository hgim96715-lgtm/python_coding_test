def solution(a, b):
    answer =0
    if a>b:
        answer=sum([n for n in range(b,a+1)])
    else:
        answer=sum([n for n in range(a,b+1)])
    return answer