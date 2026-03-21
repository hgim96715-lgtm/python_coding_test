def solution(lines):
    count = [0] * 201 
    
    for start, end in lines:
        for i in range(start, end):
            count[i + 100] += 1  
    
    answer = 0
    for c in count:
        if c >= 2:
            answer += 1
    
    return answer