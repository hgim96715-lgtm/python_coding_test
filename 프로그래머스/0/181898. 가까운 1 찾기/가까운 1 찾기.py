def solution(arr, idx):
    answer = 0
    for i,v in enumerate(arr):
        if i>=idx and arr[i]==1:
            return i
    return -1