def solution(arr):
    is_two = []
    answer=[]
    for i,v in enumerate(arr):
        if v==2 in arr:
            is_two.append(i)   
            answer=arr[is_two[0]:is_two[-1]+1]
    if len(answer)==0:
        answer.append(-1)
    return answer