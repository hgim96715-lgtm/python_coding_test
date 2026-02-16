def solution(myString, pat):
    p_l=pat.lower()
    s_l=myString.lower()
    if p_l in s_l:
        return 1
    else:
        return 0
