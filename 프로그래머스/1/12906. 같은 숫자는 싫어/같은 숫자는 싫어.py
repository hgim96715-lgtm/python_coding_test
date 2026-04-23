def solution(arr):
    answer = []
    for i in range(0,len(arr)):
        if len(answer)==0 or answer[-1]!=arr[i]:
            answer.append(arr[i])
    return answer