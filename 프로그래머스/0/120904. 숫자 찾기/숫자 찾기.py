def solution(num, k):
    num=str(num).find(str(k))
    return num+1 if num>=0 else -1