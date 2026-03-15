def solution(my_string):
    my_string = my_string.split()
    answer = int(my_string[0])
    
    for i, s in enumerate(my_string):
        if s == '+':
            answer += int(my_string[i+1])
        elif s == '-':
            answer -= int(my_string[i+1])
            
    return answer