def solution(s):
    answer = []
    closer={}
    for i,s1 in enumerate(s):
        if s1 not in closer:
            answer.append(-1)
        else:
            # print(closer)
            answer.append(i-closer[s1])
        closer[s1]=i
    return answer