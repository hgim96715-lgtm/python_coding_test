def solution(arr, queries):
    c_arr = arr[:]   

    for q in queries:
        i, j = q
        print(i,j)
        c_arr[i],c_arr[j]=c_arr[j],c_arr[i]

    return c_arr
