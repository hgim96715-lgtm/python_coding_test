def solution(strArr):
    answer = [v.upper() if i%2 else v.lower() for i,v in enumerate(strArr)]
    return answer