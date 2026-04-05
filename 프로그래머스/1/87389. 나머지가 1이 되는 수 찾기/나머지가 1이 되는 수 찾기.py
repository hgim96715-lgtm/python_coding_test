def solution(n):
    answer = []
    for k in range(1,n+1):
        if n%k==1:
            answer.append(k)
    return min(answer)