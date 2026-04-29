def solution(n):
    answer = 0
    res=''
    while n>0:
        res=str(n%3)+res
        n//=3
    res=res[::-1]
    answer=int(res,3)
    return answer