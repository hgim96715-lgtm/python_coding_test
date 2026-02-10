def solution(my_string, n):
    answer = my_string[-1:-n-1:-1]
    return answer[::-1]