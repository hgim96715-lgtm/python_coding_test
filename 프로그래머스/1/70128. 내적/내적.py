def solution(a, b):
    answer = 0
    for n, p in zip(a, b):
        answer+=(n*p)
    return answer