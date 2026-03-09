import math
def solution(box, n):
    result=math.prod([a//n for a in box])
    return result