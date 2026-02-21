from collections import Counter
def solution(strArr):
    answer = 0
    arr = [len(s) for s in strArr]
    counter = Counter(arr)
    # print(counter)
    return max(counter.values())