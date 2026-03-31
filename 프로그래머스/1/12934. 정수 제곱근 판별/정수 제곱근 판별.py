import math
def solution(n):
    answer = (math.sqrt(n)+1)**2 if int(math.sqrt(n))**2==n else -1
    return answer