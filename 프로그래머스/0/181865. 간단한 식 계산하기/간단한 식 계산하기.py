def solution(binomial):
    answer = binomial.split()
    a,b,c=answer
    if b=="+":
        return int(a)+int(c)
    elif b=="-":
        return int(a)-int(c)
    else:
        return int(a)*int(c)