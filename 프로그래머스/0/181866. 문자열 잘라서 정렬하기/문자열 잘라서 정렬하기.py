def solution(myString):
    answer = myString.strip().split("x")
    return sorted(v for v in answer if v)