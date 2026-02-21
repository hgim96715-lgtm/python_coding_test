def solution(arr, n):
    for i,v in enumerate(arr):
        if len(arr)%2:
            if i%2==0:
                 arr[i]+=n
        else:
            if i%2!=0:
                arr[i]+=n
    return arr