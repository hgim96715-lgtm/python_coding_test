def solution(n, k):
    answer = [a for a in range(1, n+1) if a % k == 0]
    # for a in range(1,n+1):
    #     if a%k==0:
    #         answer.append(a)
    return answer