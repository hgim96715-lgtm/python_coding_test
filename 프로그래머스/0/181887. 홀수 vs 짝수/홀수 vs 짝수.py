def solution(num_list):
    answer = 0
    odd=0
    even=0
    for i,v in enumerate(num_list):
        if (i+1)%2:
            odd+=v
        else:
            even+=v
    answer=max(odd,even)
    return answer