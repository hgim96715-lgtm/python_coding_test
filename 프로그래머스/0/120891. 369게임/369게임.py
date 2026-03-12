from collections import Counter
def solution(order):
    answer=0
    cnt = Counter(str(order))
    for c in  cnt.keys():
        if c in "369":
            answer+=cnt.get(c,0)
    return answer