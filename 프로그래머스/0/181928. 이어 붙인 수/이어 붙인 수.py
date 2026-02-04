def solution(num_list):
    answer = 0
    odd=""
    even=""
    for a in num_list:
        if a%2:
          odd+=str(a)
        else:
            even+=str(a)
    answer=int(odd)+int(even)
    return answer