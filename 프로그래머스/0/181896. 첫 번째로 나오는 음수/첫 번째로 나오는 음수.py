def solution(num_list):
    answer = 0
    for i,v in enumerate(num_list):
        if v<0:
            answer=i
            break
    else:
        answer=-1
    return answer