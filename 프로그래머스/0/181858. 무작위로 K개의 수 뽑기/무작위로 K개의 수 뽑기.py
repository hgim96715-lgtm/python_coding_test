def solution(arr, k):
    answer = []
    for i,v in enumerate(arr):
        if v not in answer :
            answer.append(v)
            if len(answer)==k:
                break
    while len(answer)<k:
        answer.append(-1)
    return answer