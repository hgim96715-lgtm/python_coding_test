from collections import Counter
def solution(s):
    ls=s.lower()
    c_s=Counter(ls)
    return True if c_s['p']==c_s['y'] else False