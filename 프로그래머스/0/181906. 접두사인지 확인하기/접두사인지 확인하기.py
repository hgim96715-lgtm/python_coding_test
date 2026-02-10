def solution(my_string, is_prefix):
    arr=[]
    for i,v in enumerate(my_string):
        arr.append(my_string[:i+1])
    return 1 if arr.count(is_prefix) else 0