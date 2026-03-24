def solution(common):
    answer = 0
    for a in common:
        if common[1] - common[0] == common[2] - common[1]:
            answer=common[-1]+(common[1] - common[0])
        else:
            answer=common[-1]*(common[1]//common[0])
    return answer