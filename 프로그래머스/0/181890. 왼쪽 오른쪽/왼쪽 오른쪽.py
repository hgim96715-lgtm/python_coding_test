def solution(str_list):
    answer = []
    l_in="l" in str_list
    r_in="r" in str_list
    if l_in and r_in:
        l_idx = str_list.index("l") 
        r_idx=str_list.index("r")
        if l_idx<r_idx:
            answer=str_list[:l_idx]
        else:
            answer=str_list[r_idx+1:]
    elif l_in:
        l_idx = str_list.index("l") 
        answer=str_list[:l_idx]
    elif r_in:
        r_idx=str_list.index("r")
        answer=str_list[r_idx+1:]
    return answer