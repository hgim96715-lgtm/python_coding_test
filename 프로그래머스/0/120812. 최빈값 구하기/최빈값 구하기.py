from collections import Counter

def solution(array):
    answer=0
    counter=Counter(array)
    counter_max=max(counter.values())
    for a,v in counter.items():
        if v==counter_max:
            answer+=1
            max_answer=a
    return max_answer if answer==1 else -1