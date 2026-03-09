import math
def solution(n):
    answer=0
    for a in range(10+1):
        if math.factorial(a)==n or math.factorial(a)<n:
            answer=a
    return answer