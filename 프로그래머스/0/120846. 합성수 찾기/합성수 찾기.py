from collections import Counter
def solution(n):
    answer = []
    arr=[]
    for i in range(1,n+1):
        for j in range(1,i+1):
            if i%j==0:
                answer.append(i)
    counter=Counter(answer)
    for v,c in counter.items():
        if c>=3:
            arr.append(v)
    return len(arr)