def solution(dots):
    answer = 0
    a,b,c,d=dots
    e=max(a[0],b[0],c[0],d[0])-min(a[0],b[0],c[0],d[0])
    f=max(a[1],b[1],c[1],d[1])-min(a[1],b[1],c[1],d[1])
    answer=e*f
    return answer