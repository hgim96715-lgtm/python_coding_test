def solution(arr, intervals):
    answer = []
    a,b=intervals
    a1,a2=a
    b1,b2=b
    answer=arr[a1:a2+1]+arr[b1:b2+1]
    return answer