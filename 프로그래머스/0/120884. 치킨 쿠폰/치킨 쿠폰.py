def solution(chicken):
    answer = 0
    while chicken>=10:
        a=chicken//10
        answer+=a
        chicken=a+chicken%10
    return answer