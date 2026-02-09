def solution(arr):
    stk = []
    k=0
    while k <len(arr):
        if len(stk)==0:
            stk.append(arr[k])
            k+=1
        elif len(stk)>0 and stk[-1]<arr[k]:
            stk.append(arr[k])
            k+=1
        elif len(stk)>0 and stk[-1]>=arr[k]:
            stk.pop()
    return stk