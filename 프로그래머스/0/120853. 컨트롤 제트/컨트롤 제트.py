def solution(s):
    answer = []
    arr=s.split(' ')
    for i,v in enumerate(arr):
        if v=='Z':
            answer.pop()
        else:
            answer.append(int(v))
    return sum(a for a in answer)