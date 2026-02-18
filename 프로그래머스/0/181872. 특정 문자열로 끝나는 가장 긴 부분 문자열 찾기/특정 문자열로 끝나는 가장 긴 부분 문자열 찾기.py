def solution(myString, pat):
    # answer = myString.endswith(pat)
    p=myString.rindex(pat)
    answer=myString[:p+len(pat)]
    return answer