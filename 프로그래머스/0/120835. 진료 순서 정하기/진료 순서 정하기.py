def solution(emergency):
    answer = []
    copy_e=sorted(emergency,reverse=True)
    for e in emergency:
        b=copy_e.index(e)
        answer.append(b+1)
    return answer