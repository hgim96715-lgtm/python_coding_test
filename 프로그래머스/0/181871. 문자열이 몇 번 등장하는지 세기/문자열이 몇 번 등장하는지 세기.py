def solution(myString, pat):
    answer = 0
    for i,v in enumerate(myString):
        p=myString[i:i+len(pat)]
        if p == pat:
            answer+=1
    return answer