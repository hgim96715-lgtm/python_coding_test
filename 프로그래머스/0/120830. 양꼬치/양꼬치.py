def solution(n, k):
    service=n//10
    food=12000
    dring=2000
    if service:
        return n*food+k*2000-service*2000
    else:
        return n*food+k*2000