def solution(number, limit, power):
    answer = 0
    result=[]
    for n in range(1,number+1):
        count=0
        for j in range(1, int(n ** 0.5) + 1):
            if n%j==0:
                if j * j == n:
                    count+=1
                else:
                    count+=2
        if count > limit:
            answer+=power
        else:
            answer+=count
    return answer
        
            