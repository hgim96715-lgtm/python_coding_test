def solution(s):
    answer = ''
    idx=0
    for i in s:
        if i ==' ':
            answer+=' '
            idx=0
        else:
            if idx%2:
                answer+=i.lower()
            else:
                answer+=i.upper()
            idx+=1
    return answer