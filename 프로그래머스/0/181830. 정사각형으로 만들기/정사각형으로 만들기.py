def solution(arr):
    row=len(arr)
    col=len(arr[0])
    
    if row>col:
        for ar in arr:
             ar.extend([0] * (row - col))
    elif row<col: 
        for v in range(col-row):
            arr.append([0]*col)
    return arr