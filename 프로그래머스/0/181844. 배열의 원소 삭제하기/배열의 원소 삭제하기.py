def solution(arr, delete_list):
    answer = []
    for v in arr:
        if v not in delete_list:
            answer.append(v)
    return answer