def solution(num, total):
    answer=[]
    a=(total - (num - 1) * num // 2)//num
    return [a+n for n in range(num)]