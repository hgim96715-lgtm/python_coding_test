def solution(n):
    answer = ''
    for s in '수박'*n:
        if len(answer)<n:
            answer+=s
    return answer