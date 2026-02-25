def solution(a, b):
    answer = 0
    if a%2 and b%2:
        return pow(a,2)+b**2
    elif a%2 or b%2:
        return 2*(a+b)
    else:
        return abs(a-b)
    return answer