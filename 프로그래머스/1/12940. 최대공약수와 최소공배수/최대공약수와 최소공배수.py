import math
def solution(n, m):
    ma_gc=math.gcd(n,m)
    ma_lc=(n*m)//ma_gc
    answer = [ma_gc,ma_lc]
    return answer