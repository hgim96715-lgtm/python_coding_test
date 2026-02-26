def solution(order):
    answer = 0
    for v in order:
        if 'cafelatte' in v:
            answer+=5000
        elif 'americano' in v or 'anything' in v:
            answer+=4500
    return answer