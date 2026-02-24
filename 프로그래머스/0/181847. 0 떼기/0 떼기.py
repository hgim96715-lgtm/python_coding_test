def solution(n_str):
    answer = ''
    while n_str!='' and n_str.startswith('0'):
        n_str=n_str[1:]
    return n_str