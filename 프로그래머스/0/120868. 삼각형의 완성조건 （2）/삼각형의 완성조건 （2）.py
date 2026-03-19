def solution(sides):
    answer=[]
    a,b=sides
    for c in range(abs(a-b),a+b-1):
        answer.append(c)
    return len(answer)