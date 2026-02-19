def solution(myString, pat):
    result = myString.translate(str.maketrans("AB", "BA"))
    answer = 1 if pat in result else 0
    return answer