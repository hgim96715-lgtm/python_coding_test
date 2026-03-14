def solution(s):
    answer = ''
    for v in s[:]:
        a=s.count(v)
        if a==1:
            answer+=v
    return ''.join(sorted(answer))