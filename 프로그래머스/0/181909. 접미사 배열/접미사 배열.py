def solution(my_string):
    answer = []
    for i, v in enumerate(my_string):
        answer.append(my_string[i:])
    return sorted(answer)