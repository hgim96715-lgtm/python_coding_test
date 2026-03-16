def solution(n, numlist):
    answer = [k for k in numlist if k%n==0 ]
    return answer