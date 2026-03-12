def solution(array, n):
    answer = min(array,key=lambda a:(abs(a-n),a))
    return answer