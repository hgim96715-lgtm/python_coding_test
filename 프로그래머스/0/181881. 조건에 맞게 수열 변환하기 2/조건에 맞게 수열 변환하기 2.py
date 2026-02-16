def solution(arr):
    answer = 0
    m_arr=arr[:]
    while True:
        new_arr=m_arr[:]
        for i,v in enumerate(m_arr):
            if v>=50 and v%2==0:
                m_arr[i]=v//2
            elif v<=50 and v%2!=0:
                m_arr[i]=(v*2)+1
            else:
                m_arr[i]=v
        if m_arr==new_arr:
            return answer
        answer+=1
    print(m_arr)
    return answer