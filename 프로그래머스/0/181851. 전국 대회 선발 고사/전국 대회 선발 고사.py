def solution(rank, attendance):
    answer = 0
    s_v=[]
    for i, v in enumerate(rank):
        if attendance[i]==True:
            s_v.append((i,v))
    s_v=sorted(s_v,key=lambda a:a[1])
    s_v=s_v[:3]
    (a, _), (b, _), (c, _) = s_v
    print(a, b, c)
    return (10000*a)+(100*b)+c