def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k=command
        array_cp=sorted(array[i-1:j])
        answer.append(array_cp[k-1])
    return answer