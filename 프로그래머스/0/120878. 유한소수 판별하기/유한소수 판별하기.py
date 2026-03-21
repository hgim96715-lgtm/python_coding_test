from fractions import Fraction
def solution(a, b):
    answer = 0
    f = Fraction(a, b)
    d=f.denominator
    while d%2==0:
        d//=2
    while d%5==0:
        d//=5
    if d==1:
        answer=1
    else:
        answer=2
    return answer