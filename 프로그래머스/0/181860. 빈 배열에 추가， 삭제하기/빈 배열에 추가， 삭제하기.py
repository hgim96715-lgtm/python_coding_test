def solution(arr, flag):
    answer = []
    for i,v in enumerate(arr):
        if flag[i]==True:
            answer+=[v]*v*2
        else:
            answer=answer[:-v]
    return answer