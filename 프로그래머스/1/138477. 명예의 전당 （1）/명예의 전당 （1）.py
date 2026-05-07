def solution(k, score):
    answer = []
    rever=[]
    for s in score:
        rever.append(s)
        rever.sort(reverse=True)
        if len(rever) > k:
            rever.pop()
        # print(rever,rever[-1])
        answer.append(rever[-1])
    return answer