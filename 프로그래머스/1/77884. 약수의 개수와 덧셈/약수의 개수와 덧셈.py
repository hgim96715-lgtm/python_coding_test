import math
def solution(left, right):
    answer = 0
    for k in range(left,right+1):
        if  math.sqrt(k) % 1 == 0:
            answer-=k
        else:
            answer+=k
    return answer