def solution(spell, dic):
    s=sorted(spell)
    for d in dic:
        c=sorted(d)
        if c==s:
            return 1
            break
    else:
        return 2