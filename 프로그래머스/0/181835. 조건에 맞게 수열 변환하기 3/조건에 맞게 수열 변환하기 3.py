def solution(arr, k):
    answer=[v*k if k%2 else v+k for v in arr]
    return answer