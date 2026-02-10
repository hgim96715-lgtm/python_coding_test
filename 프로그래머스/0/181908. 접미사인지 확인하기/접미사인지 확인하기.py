def solution(my_string, is_suffix):
    answer = 0
    arr=[]
    for i, v in enumerate(my_string):
        arr.append(my_string[i:])
    return 1 if arr.count(is_suffix) else 0