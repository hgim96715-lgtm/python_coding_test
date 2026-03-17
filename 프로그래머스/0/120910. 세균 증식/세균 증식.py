def solution(n, t):
    answer = n
    for a in range(1,t+1):
        answer*=2
    return answer