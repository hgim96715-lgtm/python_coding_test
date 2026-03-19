def solution(polynomial):
    x_num=0
    only_num=0
    arr = polynomial.split(' + ')
    for a in arr:
        if 'x' in a:
            b=a.replace('x','')
            if b=='':
                x_num+=1
            else:
                x_num+=int(b)
        else:
            only_num+=int(a)
    
    if x_num == 0:
        return str(only_num)
    
    x_part = 'x' if x_num == 1 else f'{x_num}x'
    
    if only_num == 0:
        return x_part
    
    return f"{x_part} + {only_num}"