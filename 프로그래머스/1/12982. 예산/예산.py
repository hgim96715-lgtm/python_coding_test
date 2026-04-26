def solution(d, budget):
    answer=0
    d.sort()
    for d1 in d:
        budget-=d1
        print(d1,budget)
        if budget>=0:
            answer+=1
        elif budget<0:
            return answer
    return answer