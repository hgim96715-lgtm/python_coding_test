def solution(str_list, ex):
    answer = ''
    for v in str_list:
        if ex in v:
            continue
        else:
            answer+=v
    return answer