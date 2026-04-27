def solution(number):
    answer = 0
    for n1 in range(len(number)):
        for n2 in range(n1+1,len(number)):
            for n3 in range(n2+1,len(number)):
                if number[n1] + number[n2] + number[n3] == 0:
                    answer+=1
    return answer