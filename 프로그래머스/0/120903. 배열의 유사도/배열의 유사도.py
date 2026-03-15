def solution(s1, s2):
    answer = 0
    for k in s1:
        for s in s2:
            if k==s:
                answer+=1
    return answer