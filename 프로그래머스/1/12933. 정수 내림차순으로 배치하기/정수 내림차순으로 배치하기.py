def solution(n):
    arr = [a for a in str(n)]
    arr2=sorted(arr,reverse=True)
    answer=''.join(arr2)
    return int(answer)