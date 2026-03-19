def solution(numbers):
    a=sorted(numbers)
    b=a[0]*a[1]
    c=a[-1]*a[-2]
    print(b,c)
    return  b if b>c else c